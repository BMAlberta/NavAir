from datetime import datetime
from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from mysql_storedprocconfig import read_stored_proc_config
import models.airport as airportModel


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route("/api/airport/list")
def list(locale):

    if locale == "default":
        return fetch_default_airports()
    else:
        print(locale)
        return fetch_airports_for_locale(locale)


def fetch_default_airports():
    proc = read_stored_proc_config('defaultAirports')
    return execute_stored_proc(proc)


def fetch_airports_for_locale(locale):
    proc = read_stored_proc_config('continentAirports')
    return execute_stored_proc(proc, locale)


def execute_stored_proc(storedproc, *args):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor(buffered=True, dictionary=True)
        for ar in args:
            param = ar

        if len(args) == 0:
            cursor.callproc(storedproc)
        else:
            cursor.callproc(storedproc, [param])

        resultobjects = []
        for recordSet in cursor.stored_results():
            for row in recordSet:
                temp = dict(zip(recordSet.column_names, row))
                resultobjects.append(dict(airportModel.Airport(temp)))

        result = {}
        result.update({"asOf":get_timestamp()})
        result.update({"airports": resultobjects})
        return result

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

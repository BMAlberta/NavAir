from datetime import datetime
from mysql.connector import MySQLConnection, Error
from util.dbconfig import read_db_config
from util.storedprocconfig import read_stored_proc_config
from flask import Blueprint, jsonify, request
import airports.model as airportmodel

airport_api = Blueprint('airport_api', __name__)


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@airport_api.route('/api/airport/list/')
def list():
    locale = request.args.get('locale')
    if locale != None:
        return fetch_airports_for_locale(locale)
    else:
        print(locale)
        return fetch_default_airports()

def fetch_default_airports():
    proc = read_stored_proc_config('defaultAirports')
    return execute_stored_proc(proc)


def fetch_airports_for_locale(locale):
    proc = read_stored_proc_config('continentAirports')
    return execute_stored_proc(proc, locale)


def execute_stored_proc(storedproc, *args):

    try:
        print("Trying to connect to the DB")
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor(buffered=True, dictionary=True)
        for ar in args:
            param = ar

        if len(args) == 0:
            cursor.callproc(storedproc)
            print("Calling defaultAirports")
        else:
            cursor.callproc(storedproc, [param])

        resultobjects = []
        for recordSet in cursor.stored_results():
            for row in recordSet:
                temp = dict(zip(recordSet.column_names, row))
                resultobjects.append(dict(airportmodel.Airport(temp)))

        result = {}
        result.update({"asOf":get_timestamp()})
        result.update({"airports": resultobjects})

        return jsonify(result)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


METAR = {
    "KCMH": {
        "icao": "KCMH",
        "airportName": "John Glenn International",
        "timestamp": get_timestamp()
    },
    "KOSU": {
        "icao": "KOSU",
        "airportName": "The Ohio State University",
        "timestamp": get_timestamp()
    }
}


def read():
    return [METAR[key] for key in sorted(METAR.keys())]

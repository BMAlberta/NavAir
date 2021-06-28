from configparser import ConfigParser


def read_stored_proc_config(proc):
    parser = read_config()
    section = 'storedproc'
    if parser.has_option(section, proc):
        return parser.get(section, proc)
    else:
        return "NAP"


def read_config():
    parser = ConfigParser()
    parser.read('config/config.ini')
    return parser


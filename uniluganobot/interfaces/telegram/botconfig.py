from configparser import ConfigParser
from functools import wraps

config_file = 'bot.cfg'

_parser = None


def ensure_loaded():
    if not _parser:
        load_config()


# decorator
def loaded(f):
    @wraps(f)
    def new_f(*args):
        ensure_loaded()
        return f(*args)
    return new_f


def read_config(filename):
    _parser = ConfigParser()
    _parser.read(filename)
    return _parser


def load_config():
    global _parser

    print('loading configuration file')
    _parser = read_config(config_file)


@loaded
def token():
    return _parser['bot']['token']

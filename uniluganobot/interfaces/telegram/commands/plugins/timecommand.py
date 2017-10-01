import datetime
from .. import Command


@Command('/time')
def echo_command(*args):
    out = datetime.datetime.now()
    return out

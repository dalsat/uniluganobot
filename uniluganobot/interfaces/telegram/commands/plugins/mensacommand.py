from .. import Command
from ..abstractcommand import AbstractCommand
from datasources.mensa import MensaSource

import datetime


@Command.register
class MensaCommand(AbstractCommand):

    command = '/mensa'
    _datasource = MensaSource()
    days = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
    lower_days = [day.lower() for day in days]

    @classmethod
    def handle_command(cls, *args):
        return cls.format(cls.data())

    @classmethod
    def format(cls, data):
        lines = []
        for key, value in data.items():
            lines.append('*%s*' % key)
            lines.append(value)
            lines.append('')

        return '\n'.join(lines)

    @classmethod
    def data(cls):
        menu = cls._datasource.data()
        weekday = datetime.date.today().weekday()

        out = menu[cls.days[weekday]]
        return out

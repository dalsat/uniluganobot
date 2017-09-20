from .. import Command
from datasources.mensa import MensaSource

import datetime


@Command('/mensa')
class MensaCommand:

    _datasource = MensaSource()
    days = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì',
            'Venerdì', 'Sabato', 'Domenica']
    lower_days = [day.lower() for day in days]

    def __call__(self, *args):
        return self.format(self.data())

    @classmethod
    def format(cls, data):
        lines = []
        for key, value in data.items():
            lines.append('*%s*' % key)
            lines.append(value)
            lines.append('')

        lines.append('')
        text = '\n'.join(lines)

        text += cls.translate_url(text)

        return text

    @staticmethod
    def translate_url(text, target_lang='en'):
        template_url = '[translate](https://translate.google.com/#it/{}/{})'
        return template_url.format(target_lang, text)

    @classmethod
    def data(cls):
        menu = cls._datasource.data()
        weekday = datetime.date.today().weekday()

        out = menu[cls.days[weekday]]
        return out

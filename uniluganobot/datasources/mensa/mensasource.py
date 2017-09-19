import requests

from ..datasource import DataSource
from .mensaparser import MensaParser


class MensaSource(DataSource):

    url = 'https://www.desk.usi.ch/en/' \
        + 'mensa-e-menu-settimanale-campus-di-lugano'
    cache_file = 'menu_cache.html'

    def __init__(self):
        self._page = None
        self._parser = None

        self.fetch_page()

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
        self._update_parser()

    def _update_parser(self):
        self._parser = MensaParser(self._page)

    def data(self) -> dict:
        return self.parse_page()

    def fetch_page(self):
        self.page = requests.get(self.url).text

    def cache_page(self, filename: str):
        with open(filename, 'w') as file:
            file.write(self._page)

    def load_page(self, filename: str):
        with open(filename, 'r') as file:
            self.page = file.read()

    def parse_page(self):
        return self._parser.parse()

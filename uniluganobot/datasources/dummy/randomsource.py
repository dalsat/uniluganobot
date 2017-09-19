from ..datasource import DataSource
import random


class RandomSource(DataSource):

    def data(self):
        return {
            'number': random.randint(0, 255)
        }

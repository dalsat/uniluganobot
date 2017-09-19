import abc


class DataSource(abc.ABC):

    @abc.abstractmethod
    def data(self) -> dict:
        """Standard method to get the data from the data source"""

from abc import ABC, abstractmethod




class IDriverService(ABC):

    @abstractmethod
    def get_all_requests(self):
        pass

    @abstractmethod
    def accept_ride(self, ride_row_key, driver_row_key) -> str:
        pass

    @abstractmethod
    def get_ride_information(self, driver_row_key):
        pass


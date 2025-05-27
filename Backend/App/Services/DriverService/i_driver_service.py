from abc import ABC, abstractmethod




class IDriverService(ABC):

    @abstractmethod
    def get_all_requests(self):
        pass

    @abstractmethod
    def accept_ride(self, ride_row_key):
        pass
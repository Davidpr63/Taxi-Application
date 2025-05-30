from abc import ABC, abstractmethod

class ITaxiLicenseTableStorage(ABC):
    @abstractmethod
    def create_or_update(self, entity):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, row_key):
        pass

    @abstractmethod
    def get_by_user_id(self, row_key) -> bool:
        pass


    @abstractmethod
    def delete_by_id(self, row_key):
        pass
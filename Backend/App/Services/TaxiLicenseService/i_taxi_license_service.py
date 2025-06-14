from abc import ABC, abstractmethod

from Backend.App.DtoModels.license_request_dto import TaxiLicenseRequestDTO



class ITaxiLicenseService(ABC):



    @abstractmethod
    def handle_request(self, user_row_key: str, licence_request_dto: TaxiLicenseRequestDTO):
        pass

    @abstractmethod
    def get_license_requests(self):
        pass
    @abstractmethod
    def approve_request(self, licence_row_key: str):
        pass

    @abstractmethod
    def reject_request(self, licence_row_key: str):
        pass

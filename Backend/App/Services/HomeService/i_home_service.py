from abc import ABC, abstractmethod

from Backend.App.DtoModels.ride_request_dto import RideRequestDTO


class IHomeService(ABC):

    @abstractmethod
    def handle_ride_request(self, ride_request_dto: RideRequestDTO, user_row_key: str) -> str:
        pass
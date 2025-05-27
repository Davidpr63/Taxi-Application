from datetime import datetime

from Backend.App.DtoModels.ride_request_dto import RideRequestDTO
from Backend.App.Models.ride import Ride
from Backend.App.Services.HomeService.i_home_service import IHomeService
from Backend.CloudStorage.TableStorage.ride_table_storage import RideTableStorage



class HomeService(IHomeService):

    def __init__(self, ride_table_storage: RideTableStorage):
        self.ride_table_storage = ride_table_storage

    def handle_ride_request(self, ride_request_dto: RideRequestDTO, user_row_key: str) -> str:
        try:
            new_ride = Ride('1',ride_request_dto.pickupAddress, ride_request_dto.destinationAddress, datetime.now(), 'Pending', user_row_key, 0)
            entity = Ride.to_entity(new_ride)
            print(entity)
            self.ride_table_storage.create_or_update(entity)
            result = "Your ride is waiting to be picked up!"
            return result
        except Exception as e:
            print('An error was occurred while handling ride request: ', e)
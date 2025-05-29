from datetime import datetime
import uuid
from operator import truediv

from Backend.App.DtoModels.ride_request_dto import RideRequestDTO
from Backend.App.Models.ride import Ride
from Backend.App.Models.ride_info import RideInfo
from Backend.App.Services.HomeService.i_home_service import IHomeService
from Backend.CloudStorage.TableStorage.ride_info_table_storage import RideInfoTableStorage
from Backend.CloudStorage.TableStorage.ride_table_storage import RideTableStorage



class HomeService(IHomeService):



    def __init__(self, ride_table_storage: RideTableStorage, ride_info_table_storage: RideInfoTableStorage):
        self.ride_table_storage = ride_table_storage
        self.ride_info_table_storage = ride_info_table_storage

    def handle_ride_request(self, ride_request_dto: RideRequestDTO, user_row_key: str) -> dict:
        try:

            new_ride = Ride(str(uuid.uuid4()),ride_request_dto.pickupAddress, ride_request_dto.destinationAddress, datetime.now(), 'Pending', user_row_key, 0)
            entity = Ride.to_entity(new_ride)
            print(entity)
            self.ride_table_storage.create_or_update(entity)
            while True:
                ride = self.ride_table_storage.get_by_id(new_ride.ride_id)
                if ride['Status'] == 'Accepted':
                    self.ride_table_storage.delete_by_id(new_ride.ride_id)
                    break
            ride_info = self.ride_info_table_storage.get_by_user_id(ride['UserId'])
            message = 'success'
            result = {
                'message': message,
                'rideInfo': ride_info
            }
            return result
        except Exception as e:
            print('An error was occurred while handling ride request: ', e)

    def get_ride_info(self, user_row_key: str):
        try:
            ride_info = RideInfo.from_entity(self.ride_info_table_storage.get_by_user_id(user_row_key))
            ride_info_dto = RideInfo.driver_info_for_ride_to_dto(ride_info).dict()
            return ride_info_dto
        except Exception as e:
            print("An error was occurred while trying to get information about the ride: ", e)
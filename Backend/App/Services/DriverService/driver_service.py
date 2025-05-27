from multiprocessing.forkserver import read_signed

from Backend.App.Models.ride import Ride
from Backend.App.Services.DriverService.i_driver_service import IDriverService
from Backend.CloudStorage.TableStorage.ride_table_storage import RideTableStorage
from Backend.CloudStorage.TableStorage.user_table_storage import UserTableStorage


class DriverService(IDriverService):


    def __init__(self, ride_table_storage: RideTableStorage, user_table_storage: UserTableStorage):
        self.ride_table_storage = ride_table_storage
        self.user_table_storage = user_table_storage

    def get_all_requests(self):
        try:
            result = []
            all_rides = self.ride_table_storage.get_all()
            for ride in all_rides:
                first_name = self.user_table_storage.get_by_id(ride['UserId'])['FirstName']
                last_name = self.user_table_storage.get_by_id(ride['UserId'])['LastName']
                ride_dto = Ride.to_dto(Ride.from_entity(ride), first_name, last_name).dict()
                result.append(ride_dto)

            return result
        except Exception as e:
            print('An error occurred while trying to fetch all ride', e)

    def accept_ride(self, ride_row_key):
        pass

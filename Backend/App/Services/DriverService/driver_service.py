import uuid
from Backend.App.Models.driver import Driver
from Backend.App.Models.ride import Ride
from Backend.App.Models.ride_info import RideInfo
from Backend.App.Services.DriverService.i_driver_service import IDriverService
from Backend.CloudStorage.TableStorage.driver_table_storage import DriverTableStorage
from Backend.CloudStorage.TableStorage.ride_info_table_storage import RideInfoTableStorage
from Backend.CloudStorage.TableStorage.ride_table_storage import RideTableStorage
from Backend.CloudStorage.TableStorage.user_table_storage import UserTableStorage


class DriverService(IDriverService):



    def __init__(self, ride_table_storage: RideTableStorage, user_table_storage: UserTableStorage, driver_table_storage: DriverTableStorage, ride_info_table_storage: RideInfoTableStorage):
        self.ride_table_storage = ride_table_storage
        self.user_table_storage = user_table_storage
        self.driver_table_storage = driver_table_storage
        self.ride_info_table_storage = ride_info_table_storage

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

    def accept_ride(self, ride_row_key, driver_rok_key) -> str:
        try:
            message = ''
            ride = Ride.from_entity(self.ride_table_storage.get_by_id(ride_row_key))
            if ride.status == "Pending":
                ride.status = "Accepted"
                ride.driver_id = driver_rok_key
                self.ride_table_storage.create_or_update(Ride.to_entity(ride))
                self.create_ride_info(ride.user_id, driver_rok_key)
                message = "success"
                return message
            else:
                message = "Cannot accept a ride, because It has accepted already."
                return message
        except Exception as e:
            print("An error occurred during accepting the ride: ", e)


    def get_ride_information(self, driver_row_key):
        try:
            driver_info = Driver.from_entity(self.driver_table_storage.get_by_id(driver_row_key))
            dto = Driver.driver_info_for_ride_to_dto(driver_info).dict()
            return dto
        except Exception as e:
            print("An error was occurred while trying to get data for driver: ", e)

    def create_ride_info(self, user_id, driver_row_key):
        driver = Driver.from_entity(self.driver_table_storage.get_by_id(driver_row_key))
        ride_info = RideInfo(str(uuid.uuid4()), driver.first_name, driver.last_name, driver.car, 5, user_id)
        self.ride_info_table_storage.create_or_update(RideInfo.to_entity(ride_info))
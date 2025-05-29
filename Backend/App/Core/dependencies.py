from fastapi import Depends

from Backend.App.Services.AuthUserService.auth_user_service import AuthUserService
from Backend.App.Services.DriverService.driver_service import DriverService
from Backend.App.Services.HomeService.home_service import HomeService
from Backend.App.Services.UserService.user_service import UserService
from Backend.CloudStorage.TableStorage.driver_table_storage import DriverTableStorage
from Backend.CloudStorage.TableStorage.ride_info_table_storage import RideInfoTableStorage
from Backend.CloudStorage.TableStorage.ride_table_storage import RideTableStorage
from Backend.CloudStorage.TableStorage.user_table_storage import UserTableStorage


def get_user_table_storage():
    return UserTableStorage()
def get_ride_table_storage():
    return RideTableStorage()
def get_driver_table_storage():
    return DriverTableStorage()
def get_ride_info_table_storage():
    return RideInfoTableStorage()

def get_auth_service(user_table_storage: UserTableStorage = Depends(get_user_table_storage)):
    return AuthUserService(user_table_storage)

def get_user_service(user_table_storage: UserTableStorage = Depends(get_user_table_storage)):
    return UserService(user_table_storage)

def get_home_service(ride_table_storage: RideTableStorage = Depends(get_ride_table_storage), ride_info_table_storage: RideInfoTableStorage = Depends(get_ride_info_table_storage)):
    return HomeService(ride_table_storage, ride_info_table_storage)

def get_driver_service(
        ride_table_storage: RideTableStorage = Depends(get_ride_table_storage),
        user_table_storage: UserTableStorage = Depends(get_user_table_storage),
        driver_table_storage: DriverTableStorage = Depends(get_driver_table_storage),
        ride_info_table_storage: RideInfoTableStorage = Depends(get_ride_info_table_storage)
    ):
    return DriverService(ride_table_storage, user_table_storage, driver_table_storage, ride_info_table_storage)


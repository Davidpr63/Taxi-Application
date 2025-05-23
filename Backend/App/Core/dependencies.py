from fastapi import Depends

from Backend.App.Services.AuthUserService.auth_user_service import AuthUserService
from Backend.App.Services.UserService.user_service import UserService
from Backend.CloudStorage.TableStorage.user_table_storage import UserTableStorage


def get_user_table_storage():
    return UserTableStorage()

def get_auth_service(user_table_storage: UserTableStorage = Depends(get_user_table_storage)):
    return AuthUserService(user_table_storage)

def get_user_service(user_table_storage: UserTableStorage = Depends(get_user_table_storage)):
    return UserService(user_table_storage)
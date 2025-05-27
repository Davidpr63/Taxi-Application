
from Backend.App.Models.user import User
from Backend.App.Services.UserService.i_user_service import IUserService
from Backend.App.Utils.Security.security import Security
from Backend.CloudStorage.TableStorage.user_table_storage import UserTableStorage

security = Security()
class UserService(IUserService):

    def __init__(self, user_table_storage: UserTableStorage):
        self.user_table_storage = user_table_storage
        pass

    def get_user_data(self, row_key: str) -> dict:
        try:
            user = User.from_entity(self.user_table_storage.get_by_id(row_key))

            user_profile_dto = User.to_dto(user)

            return user_profile_dto.dict()
        except Exception as e:
            print("An error was occurred while trying to get data for user: ", e)

    def update_user_data(self, row_key, new_user_data_dto) -> str:
        try:
            message = self.is_valid(row_key, new_user_data_dto)
            print('message', message)
            if message == "success":
                new_user_data = User.from_dto(new_user_data_dto)
                user = User.from_entity(self.user_table_storage.get_by_id(row_key))
                if new_user_data.password != "":
                    new_user_data.password = security.hash_password(new_user_data.password)
                else:
                    new_user_data.password = user.password
                user.update_data(new_user_data)
                self.user_table_storage.create_or_update(new_user_data.updated_user_data_to_entity(row_key))
                return message
            else:
                return message
        except Exception as e:
            print('An error occurred while updating user data :', e)

    def is_valid(self, row_key, new_data_dto) -> str:
        result = "success"
        try:
            old_user = self.user_table_storage.get_by_id(row_key)
            if old_user['Username'] != new_data_dto.username:
                user_exist = self.user_table_storage.get_by_username(new_data_dto.username)
                if user_exist:
                    result = "The username already exists. Please choose a different one."
                    return result
            if new_data_dto.password or new_data_dto.confirm_password:
                if new_data_dto.password != new_data_dto.confirm_password:
                    result = "Password and confirm password don't match"
                    return result

            return result
        except Exception as e:
            print('Is valid new data for user error : ', e)



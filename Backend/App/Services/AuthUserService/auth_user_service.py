from datetime import timedelta

from Backend.App.DtoModels.login_user_dto import LoginUserDTO
from Backend.App.DtoModels.user_dto import RegisterUserDTO
from Backend.App.Models.user import User
from Backend.App.Models.user_type import UserType
from Backend.App.Utils.Jwt import jwt_config
from Backend.App.Services.AuthUserService.i_auth_user_service import IAuthUserService
from Backend.App.Utils.Security.security import Security
from Backend.CloudStorage.TableStorage.user_table_storage import UserTableStorage

security = Security()
class AuthUserService(IAuthUserService):


    def __init__(self, user_table_storage: UserTableStorage):
        self.user_table_storage = user_table_storage

    def register(self, dto: RegisterUserDTO):
        try:
            message = self.is_valid(dto)
            print('message', message)
            if message == "success":
                new_user = User.from_dto(dto)
                new_user.password = security.hash_password(new_user.password)
                new_user.user_type = UserType.USER
                self.user_table_storage.create_or_update(new_user.to_entity())
                return message
            else:
                return message
        except Exception as e:
            print('An error occurred during user registration :', e)

    def is_valid(self, dto: RegisterUserDTO) -> str:
        result = "success"
        try:

            user_exist = self.user_table_storage.get_by_username(dto.username)
            print("postoji", user_exist)
            if user_exist:
                result = "The username already exists. Please choose a different one."
                return result

            if dto.password != dto.confirm_password:
                result = "Password and confirm password don't match"
                return result

            return result
        except Exception as e:
            print('is valid error : ', e)

    def login(self, dto: LoginUserDTO) -> dict:
        try:
            message = {
                "result": "success",
                "jwt": ""
            }
            all_user = self.user_table_storage.get_all()
            exist_user = [
                user for user in all_user
                if user["Username"] == dto.username and security.verify_password(dto.password, user["Password"])
            ]
            if exist_user:
                message["jwt"] = jwt_config.create_access_token(
                    data={"sub": exist_user[0]['RowKey'], "role": exist_user[0]['UserType']},
                    expires_delta=timedelta(minutes=30)
                )
                return message
            else:
                message["result"] = "Invalid username or password"
                return message
        except Exception as e:
            print("An error occurred during logging user: ", e)



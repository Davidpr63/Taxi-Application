from Backend.App.DtoModels.new_user_data import NewUserDataDTO
from Backend.App.DtoModels.user_dto import RegisterUserDTO
import uuid

from Backend.App.DtoModels.user_profile_dto import UserProfileDTO
from Backend.App.Models.user_type import UserType


class User:

    PARTITION_KEY = "user"

    def __init__(self,
                 user_id: str,
                 first_name: str,
                 last_name :str,
                 username :str,
                 password :str,
                 confirm_password: str,
                 phone_number :str,
                 user_type: UserType
                 ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.confirm_password = confirm_password,
        self.phone_number = phone_number
        self.user_type = user_type

    # for cloud storage
    def to_entity(self) -> dict:
        return {
            "PartitionKey": self.PARTITION_KEY,
            "RowKey": str(uuid.uuid4()),
            "FirstName":self.first_name,
            "LastName":self.last_name,
            "Username":self.username,
            "Password":self.password,
            "PhoneNumber":self.phone_number,
            "UserType":self.user_type
        }

    # from cloud storage
    @classmethod
    def from_entity(cls, entity: dict):
        return cls(
            user_id=entity.get('RowKey'),
            first_name=entity.get('FirstName'),
            last_name=entity.get('LastName'),
            username=entity.get('Username'),
            password=entity.get('Password'),
            confirm_password='',
            phone_number=entity.get('PhoneNumber'),
            user_type=entity.get('UserType')
        )

    def change_user_role(self, new_role: UserType):
        self.user_type = new_role

    def update_data(self, new_user_data):
        self.first_name = new_user_data.first_name
        self.last_name = new_user_data.last_name
        self.username = new_user_data.username
        self.password = new_user_data.password
        self.phone_number = new_user_data.phone_number

    def updated_user_data_to_entity(self, row_key) -> dict:
        return {
            "PartitionKey": self.PARTITION_KEY,
            "RowKey": row_key,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Username": self.username,
            "Password": self.password,
            "PhoneNumber": self.phone_number,
            "UserType": self.user_type
        }

    def to_dto(self) -> UserProfileDTO:
        return UserProfileDTO(
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            phone_number=self.phone_number
        )

    @classmethod
    def from_dto(cls, dto: RegisterUserDTO):
        return cls(
            user_id="",
            first_name=dto.first_name,
            last_name=dto.last_name,
            username=dto.username,
            password=dto.password,
            confirm_password=dto.confirm_password,
            phone_number=dto.phone_number,
            user_type=UserType.USER
        )

    @classmethod
    def from_new_user_data_dto(cls, dto: NewUserDataDTO):
        return cls(
            first_name=dto.first_name,
            last_name=dto.last_name,
            username=dto.username,
            password=dto.password,
            confirm_password=dto.confirm_password,
            phone_number=dto.phone_number
        )





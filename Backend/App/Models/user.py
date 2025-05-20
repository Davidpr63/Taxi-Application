from Backend.App.DtoModels.userDTO import RegisterUserDTO
import uuid

class User:

    PARTITION_KEY = "user"

    def __init__(self,
                 user_id: str,
                 first_name: str,
                 last_name :str,
                 username :str,
                 password :str,
                 confirm_password: str,
                 phone_number :str
                 ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.confirm_password = confirm_password,
        self.phone_number = phone_number

    def to_entity(self) -> dict:
        return {
            "PartitionKey": self.PARTITION_KEY,
            "RowKey": str(uuid.uuid4()),
            "FirstName":self.first_name,
            "LastName":self.last_name,
            "Username":self.username,
            "Password":self.password,
            "PhoneNumber":self.phone_number
        }
    @classmethod
    def from_entity(cls, entity: dict):
        return cls(
            user_id=entity["RowKey", " "],
            first_name=entity["FirstName", " " ],
            last_name=entity["LastName", " "],
            username=entity["Username", " "],
            password=entity["Password", " "],
            confirm_password="",
            phone_number=entity["PhoneNumber", " "]
        )

    def to_dto(self) -> RegisterUserDTO:
        return UserDTO(
            user_id=self.user_id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            password="",
            confirm_password="",
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
            phone_number=dto.phone_number
        )





from pydantic import BaseModel


class RegisterUserDTO(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    confirm_password: str
    phone_number: str
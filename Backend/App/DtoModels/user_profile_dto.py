from pydantic import BaseModel


class UserProfileDTO(BaseModel):
    first_name: str
    last_name: str
    username: str
    phone_number: str
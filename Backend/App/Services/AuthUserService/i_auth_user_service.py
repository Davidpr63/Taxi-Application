from abc import ABC, abstractmethod

from Backend.App.DtoModels.LoginUserDTO import LoginUserDTO
from Backend.App.DtoModels.userDTO import RegisterUserDTO


class IAuthUserService(ABC):

    @abstractmethod
    def register(self, dto: RegisterUserDTO):
        pass

    @abstractmethod
    def is_valid(self, dto: RegisterUserDTO) -> str:
        pass
    @abstractmethod
    def login(self, dto: LoginUserDTO) -> dict:
        pass

    @abstractmethod
    def hash_password(self, plain_password: str) -> str:
        pass

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        pass
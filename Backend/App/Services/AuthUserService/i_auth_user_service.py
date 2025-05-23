from abc import ABC, abstractmethod

from Backend.App.DtoModels.login_user_dto import LoginUserDTO
from Backend.App.DtoModels.user_dto import RegisterUserDTO


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


from abc import ABC, abstractmethod

from Backend.App.DtoModels.user_profile_dto import UserProfileDTO


class IUserService(ABC):

    @abstractmethod
    def get_user_data(self, row_key: str) -> UserProfileDTO:
        pass

    @abstractmethod
    def update_user_data(self, row_key, new_data_dto) -> str:
        pass

    @abstractmethod
    def is_valid(self, row_key, new_data_dto) -> str:
        pass
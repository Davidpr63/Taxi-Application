import uuid
from email import message_from_binary_file

from Backend.App.DtoModels.license_dto import LicenseDTO
from Backend.App.DtoModels.license_request_dto import TaxiLicenseRequestDTO
from Backend.App.Models.taxi_license import TaxiLicense
from Backend.App.Models.user import User
from Backend.App.Models.user_type import UserType
from Backend.App.Services.TaxiLicenseService.i_taxi_license_service import ITaxiLicenseService
from Backend.CloudStorage.TableStorage.taxi_license_table_storage import TaxiLicenseTableStorage
from Backend.CloudStorage.TableStorage.user_table_storage import UserTableStorage


class TaxiLicenseService(ITaxiLicenseService):

    def __init__(self, taxi_license_table_storage: TaxiLicenseTableStorage, user_table_storage: UserTableStorage):
        self.taxi_license_table_storage = taxi_license_table_storage
        self.user_table_storage = user_table_storage

    def accept_request(self, user_row_key: str, licence_request_dto: TaxiLicenseRequestDTO):
        try:
            if not self.taxi_license_table_storage.get_by_user_id(user_row_key):
                taxi_license = TaxiLicense(str(uuid.uuid4()), licence_request_dto.car, licence_request_dto.licensePlate, licence_request_dto.email,'Pending', user_row_key)
                self.taxi_license_table_storage.create_or_update(TaxiLicense.to_entity(taxi_license))
                message = 'success'
                return message
            else :
                message = "You have license already"
                return message
        except Exception as e:
            print("An error was occurred while trying to accept request for driver: ", e)
            message = 'error'
            return message

    def get_license_requests(self):
        try:
            result = []
            license_requests = self.taxi_license_table_storage.get_all()
            for license in license_requests:
                license_dto = self.create_dto(TaxiLicense.from_entity(license))
                result.append(license_dto)

            return result

        except Exception as e:
            print("An error was occurred while trying to fetch license requests", e)

    def approve_driver(self, licence_row_key: str):
        try:

            license = TaxiLicense.from_entity(self.taxi_license_table_storage.get_by_id(licence_row_key))
            license.status = 'Accepted'
            self.taxi_license_table_storage.create_or_update(TaxiLicense.to_entity(license))
            user = User.from_entity(self.user_table_storage.get_by_id(license.user_id))
            user.user_type = UserType.DRIVER
            self.user_table_storage.create_or_update(User.to_entity(user))
            print(4)
        except Exception as e:
            print('An error was occured while trying to approve driver', e)

    def create_dto(self, license: TaxiLicense) -> dict:
        user = self.user_table_storage.get_by_id(license.user_id)
        dto = LicenseDTO(license.license_id, user['FirstName'], user['LastName'], license.email, user['PhoneNumber'],
                         license.car, license.license_plate, license.status)

        return dto.to_dict()
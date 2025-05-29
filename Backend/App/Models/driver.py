from Backend.App.DtoModels.ride_information_dto import RideInformationDTO

PARTITION_KEY = 'driver'
class Driver():

    def __init__(self, driver_id, first_name, last_name, car, email):
        self.driver_id = driver_id
        self.first_name = first_name
        self.last_name = last_name
        self.car = car
        self.email = email

    def to_entity(self) -> dict:
        return {
            "PartitionKey": PARTITION_KEY,
            "RowKey": self.driver_id,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Car": self.car,
            "Email": self.email
        }

    # from cloud storage

    @classmethod
    def from_entity(cls, entity: dict):
        return cls(
            driver_id = entity.get("RowKey"),
            first_name=entity.get("FirstName"),
            last_name=entity.get("LastName"),
            car=entity.get("Car"),
            email=entity.get("Email")
        )

    def driver_info_for_ride_to_dto(self) -> RideInformationDTO:
        return RideInformationDTO(
            firstName= self.first_name,
            lastName= self.last_name,
            car= self.car
        )

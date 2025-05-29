from Backend.App.DtoModels.ride_information_dto import RideInformationDTO

PARTITION_KEY = 'rideinfo'
class RideInfo:

    def __init__(self, ride_info_id, driver_first_name, driver_last_name, driver_car, eta, user_id):
        self.ride_info_id = ride_info_id
        self.driver_first_name = driver_first_name
        self.driver_last_name = driver_last_name
        self.driver_car = driver_car
        self.eta = eta # eta -> Estimate Time of Arrival
        self.user_id = user_id

    def to_entity(self) -> dict:
        return {
            "PartitionKey": PARTITION_KEY,
            "RowKey": self.ride_info_id,
            "DriverFirstName": self.driver_first_name,
            "DriverLastName": self.driver_last_name,
            "DriverCar": self.driver_car,
            "ETA":self.eta,
            "UserId": self.user_id
        }

    # from cloud storage

    @classmethod
    def from_entity(cls, entity: dict):
        return cls(
            ride_info_id = entity.get("RowKey"),
            driver_first_name=entity.get("DriverFirstName"),
            driver_last_name=entity.get("DriverLastName"),
            driver_car=entity.get("DriverCar"),
            eta= entity.get("ETA"),
            user_id=entity.get("UserId")
        )

    def driver_info_for_ride_to_dto(self) -> RideInformationDTO:
        return RideInformationDTO(
            DriverFirstName= self.driver_first_name,
            DriverLastName= self.driver_last_name,
            DriverCar= self.driver_car,
            ETA= self.eta
        )

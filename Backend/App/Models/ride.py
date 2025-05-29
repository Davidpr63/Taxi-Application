import uuid
from datetime import datetime
from Backend.App.DtoModels.ride_dto import RideDTO

PARTITION_KEY = 'ride'

class Ride:
    def __init__(self, ride_id, pickup_address, destination_address, datetime, status, user_id, driver_id):
        self.ride_id = ride_id
        self.pickup_address = pickup_address
        self.destination_address = destination_address
        self.datetime = datetime
        self.status = status
        self.user_id = user_id
        self.driver_id = driver_id

    def to_dto(self, first_name, last_name) -> RideDTO:
        return RideDTO(
            rideId = self.ride_id,
            passangerFirstname = first_name,
            passangerLastname = last_name,
            pickupAddress = self.pickup_address,
            destinationAddress = self.destination_address,
            datetime=str(self.datetime),
            status = self.status
        )
    def to_entity(self) -> dict:
        return {
            "PartitionKey": PARTITION_KEY,
            "RowKey": self.ride_id,
            "PickupAddress":self.pickup_address,
            "DestinationAddress":self.destination_address,
            "DateTime":self.datetime,
            "Status":self.status,
            "UserId":self.user_id,
            "DriverId":self.driver_id
        }

    @classmethod
    def from_entity(cls, entity: dict):
        return cls(
            ride_id = entity.get('RowKey'),
            pickup_address = entity.get('PickupAddress'),
            destination_address = entity.get('DestinationAddress'),
            datetime = entity.get('DateTime'),
            status=entity.get('Status'),
            user_id = entity.get('UserId'),
            driver_id = entity.get('DriverId')
        )

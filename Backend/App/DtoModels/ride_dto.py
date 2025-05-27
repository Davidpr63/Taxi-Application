from pydantic import BaseModel


class RideDTO(BaseModel):
    rideId: str
    passangerFirstname: str
    passangerLastname: str
    pickupAddress: str
    destinationAddress: str
    datetime: str
    status: str



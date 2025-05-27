from pydantic import BaseModel


class RideRequestDTO(BaseModel):
    pickupAddress: str
    destinationAddress : str
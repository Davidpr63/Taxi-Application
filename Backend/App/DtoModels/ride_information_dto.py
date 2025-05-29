from pydantic import BaseModel


class RideInformationDTO(BaseModel):
    DriverFirstName:str
    DriverLastName:str
    DriverCar:str
    ETA: int # Estimate Time of Arrival

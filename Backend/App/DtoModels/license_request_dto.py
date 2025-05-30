from pydantic import BaseModel


class TaxiLicenseRequestDTO(BaseModel):
    car: str
    licensePlate: str
    email: str
from pydantic import BaseModel


class LicenseIdDTO(BaseModel):
    licenseId : str
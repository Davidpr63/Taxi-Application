


class LicenseDTO:

    def __init__(self, taxiLicenseId, userFirstName, userLastname, userEmail, userPhone, userCar, licensePlate, userStatus):
        self.taxiLicenseId = taxiLicenseId
        self.userFirsName = userFirstName
        self.userLastName = userLastname
        self.userEmail = userEmail
        self.userPhone = userPhone
        self.userCar = userCar
        self.licensePlate = licensePlate
        self.userStatus = userStatus

    def to_dict(self):
        return {
            "taxiLicenseId": self.taxiLicenseId,
            "userFirstName": self.userFirsName,
            "userLastName": self.userLastName,
            "userEmail": self.userEmail,
            "userPhone": self.userPhone,
            "userCar": self.userCar,
            "licensePlate": self.licensePlate,
            "userStatus": self.userStatus
        }


    



PARTITION_KEY = 'license'
class TaxiLicense:

    def __init__(self, license_id, car, license_plate, email, status, user_id):
        self.license_id = license_id
        self.car = car
        self.license_plate = license_plate
        self.email = email
        self.status = status
        self.user_id = user_id



    def to_entity(self) -> dict:
        return {
            "PartitionKey": PARTITION_KEY,
            "RowKey": self.license_id,
            "Car": self.car,
            "LicensePlate": self.license_plate,
            "Email": self.email,
            "Status":self.status,
            "UserId": self.user_id
        }

    # from cloud storage

    @classmethod
    def from_entity(cls, entity: dict):
        return cls(
            license_id = entity.get("RowKey"),
            car=entity.get("Car"),
            email=entity.get("Email"),
            status=entity.get("Status"),
            license_plate=entity.get('LicensePlate'),
            user_id=entity.get("UserId")
        )




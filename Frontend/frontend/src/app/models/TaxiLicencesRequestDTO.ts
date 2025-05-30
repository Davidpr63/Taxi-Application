export interface TaxiLicenseRequestDTO {
    car: string;
    licensePlate:string;
    email: string;
}

export interface LicenseDTO {
    taxiLicenseId : string;
    userFirstName: string;
    userLastName: string;
    userEmail: string;
    userPhone: string;
    userCar: string;
    licensePlate: string;
    userStatus: string;
}

export interface LicenseIdDTO {
    licenseId: string;
}
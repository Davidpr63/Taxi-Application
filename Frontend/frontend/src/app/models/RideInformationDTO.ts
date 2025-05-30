export interface RideInformationDTO {
    DriverFirstName: string;
    DriverLastName: string;
    DriverCar: string;
    ETA: number;
}

export interface RideAcceptedDTO {
    firstName: string;
    lastName: string;
    car: string;
    eta: number; // Estimate Time of Arrival
}
export interface RideInformationDTO {
    firstName: string;
    lastName: string;
    car: string;
    ETA: number;
}

export interface RideAcceptedDTO {
    firstName: string;
    lastName: string;
    car: string;
    eta: number; // Estimate Time of Arrival
}
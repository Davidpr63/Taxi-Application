export interface RegisterUserDTO {
    first_name: string;
    last_name: string;
    username: string;
    password: string;
    confirm_password: string;
    phone_number: string;
}
export interface LoginUserDTO {  
    username: string;
    password: string;
    
}
export interface UserProfileDTO {
    first_name: string;
    last_name: string;
    username: string;
    phone_number: string;
}
export interface NewUserDataDTO {
    first_name: string;
    last_name: string;
    username: string;
    password: string;
    confirm_password: string;
    phone_number: string;
}

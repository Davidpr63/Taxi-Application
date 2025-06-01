import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {  NewUserDataDTO, UserProfileDTO } from '../../models/UserDTO';
import { enviroment } from '../../../enviroments/envitoment';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private apiUrl = enviroment.apiUrlUser;

  constructor(private http: HttpClient) { }

  GetUserData(): Observable<UserProfileDTO> {
    const jwt_token = localStorage.getItem('jwt_token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${jwt_token}`
    })

    return this.http.get<UserProfileDTO>(`${this.apiUrl}/my-profile`, { headers })
  } 

  updateUserData(new_user_data_dto: NewUserDataDTO) : Observable<any>{
    const jwt_token = localStorage.getItem('jwt_token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${jwt_token}`
    })

     return this.http.post(`${this.apiUrl}/update-user`, new_user_data_dto, {headers});
  }
}

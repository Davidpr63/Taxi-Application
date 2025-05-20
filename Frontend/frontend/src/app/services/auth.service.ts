import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginUserDTO, RegisterUserDTO } from '../models/UserDTO';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = "http://localhost:8000/api/auth";
  
  constructor(private http: HttpClient) { }

  register(RegisterUserDTO: RegisterUserDTO): Observable<any>{
    return this.http.post(`${this.apiUrl}/registration`, RegisterUserDTO);
  }

  login(loginDTO: LoginUserDTO): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, loginDTO)
  }
}

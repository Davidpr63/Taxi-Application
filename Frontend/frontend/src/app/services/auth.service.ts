import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginUserDTO, RegisterUserDTO } from '../models/UserDTO';
import { BehaviorSubject, Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = "http://localhost:8000/api/auth";

  private loggedIn = new BehaviorSubject<boolean>(this.isLoggedIn());
  isLoggedIn$ = this.loggedIn.asObservable();

  private userRole = new BehaviorSubject<string | null>(this.getRoleFromToken());
  userRole$ = this.userRole.asObservable();
  
  constructor(private http: HttpClient, private router: Router) { }

  register(RegisterUserDTO: RegisterUserDTO): Observable<any>{
    return this.http.post(`${this.apiUrl}/registration`, RegisterUserDTO);
  }

  login(loginDTO: LoginUserDTO): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, loginDTO)
  }
  
  logout(){ 
    localStorage.removeItem('jwt_token')
    this.loggedIn.next(false);
    this.router.navigate(['/login'])
  }
    saveToken(token: string){
    localStorage.setItem('jwt_token', token)
    this.loggedIn.next(true);
  }

  getToken(): string | null {
    return localStorage.getItem('jwt_token')
  }

  getRoleFromToken(): string | null {
  const token = localStorage.getItem('jwt_token');
  if (!token) return null;

  const payload = JSON.parse(atob(token.split('.')[1]));

  return payload.role || null;
}

  isLoggedIn() : boolean {
    return !!localStorage.getItem('jwt_token');
  }
}

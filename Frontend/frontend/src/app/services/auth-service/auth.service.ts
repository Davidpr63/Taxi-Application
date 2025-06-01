import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginUserDTO, RegisterUserDTO } from '../../models/UserDTO';
import { BehaviorSubject, Observable } from 'rxjs';
import { Router } from '@angular/router';
import { UserType } from '../../models/UserType';
import { enviroment } from '../../../enviroments/envitoment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = enviroment.apiUrlAuth;

  private loggedIn = new BehaviorSubject<boolean>(this.isLoggedIn());
  private role = new BehaviorSubject<string | null>(this.getRoleFromToken());
  private userRole:string = 'user'
  isLoggedIn$ = this.loggedIn.asObservable();
  userRole$ = this.role.asObservable();
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
    this.role.next(this.getRoleFromToken())
    this.router.navigate(['/login'])
  }

  saveToken(token: string){
    localStorage.setItem('jwt_token', token)
    this.loggedIn.next(true);
    this.role.next(this.getRoleFromToken())
  }

  getToken(): string | null {
    return localStorage.getItem('jwt_token')
  }
  
  getUserIdFromToken(): string | null {
  const token = localStorage.getItem('jwt_token');
   if(!token)
    return null
 
    const payload = JSON.parse(atob(token.split('.')[1]));
    
    return payload.sub || null
     
   
}
  getRoleFromToken(): string | null {
  const token = localStorage.getItem('jwt_token');
  if (!token) return null;

  const payload = JSON.parse(atob(token.split('.')[1]));
  
  if (payload.role === 'UserType.USER'){
    this.userRole = 'user'
    return this.userRole;
  }
    
  else if (payload.role === 'UserType.DRIVER'){
    this.userRole = 'driver'
    return this.userRole;
  }
  else {
    this.userRole = 'admin'
    return this.userRole;
  }
    
  
}

  isLoggedIn() : boolean {
    return !!localStorage.getItem('jwt_token');
  }
}

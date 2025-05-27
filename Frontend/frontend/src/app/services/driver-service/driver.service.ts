import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { RidesDTO } from '../../models/RidesDTO';

@Injectable({
  providedIn: 'root'
})
export class DriverService {

  private apiUrl = "http://localhost:8000/api/driver";

  constructor(private http: HttpClient) { }

  getRideRequests(): Observable<any>{

    const jwt_token = localStorage.getItem('jwt_token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${jwt_token}`
    })

    return this.http.get<any>(`${this.apiUrl}/get-ride-requests`, { headers })
  }
}

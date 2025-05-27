import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { RideRequestDTO } from '../../models/RideRequest';
import { AuthService } from '../auth-service/auth.service';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  private apiUrl = "http://localhost:8000/api/home";
  
  constructor(private http: HttpClient) { }


  rideRequest(ride_request_dto: RideRequestDTO): Observable<any>{
    const jwt_token = localStorage.getItem('jwt_token');
      const headers = new HttpHeaders({
        'Authorization': `Bearer ${jwt_token}`
      })

    return this.http.post(`${this.apiUrl}/ride-request`, ride_request_dto, { headers })

  }

}

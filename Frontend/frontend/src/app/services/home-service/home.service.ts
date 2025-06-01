import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { RideRequestDTO } from '../../models/RideRequest';
import { enviroment } from '../../../enviroments/envitoment';
 

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  private apiUrl = enviroment.apiUrlHome;


  constructor(private http: HttpClient) { }


  sendRideRequest(ride_request_dto: RideRequestDTO): Observable<any>{
    const jwt_token = localStorage.getItem('jwt_token');
      const headers = new HttpHeaders({
        'Authorization': `Bearer ${jwt_token}`
      })

    return this.http.post(`${this.apiUrl}/ride-request`, ride_request_dto, { headers })

  }
 
  getRideInfo(): Observable<any>{

    const jwt_token = localStorage.getItem('jwt_token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${jwt_token}`
    })

    return this.http.get<any>(`${this.apiUrl}/get-ride-info`, { headers })
  }
}

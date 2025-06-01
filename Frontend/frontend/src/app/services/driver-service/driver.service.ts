import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, Subject } from 'rxjs';
import { RideIdDTO, RidesDTO } from '../../models/RidesDTO';
import { enviroment } from '../../../enviroments/envitoment';


@Injectable({
  providedIn: 'root'
})
export class DriverService {

   
  private apiUrl = enviroment.apiUrlDriver;

  private rideAccepted = new Subject<number>();
  rideAccepted$ = this.rideAccepted.asObservable();

  constructor(private http: HttpClient) { }

  getRideRequests(): Observable<any>{

    const jwt_token = localStorage.getItem('jwt_token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${jwt_token}`
    })

    return this.http.get<any>(`${this.apiUrl}/get-ride-requests`, { headers })
  }

  acceptRide(ride_id_dto : RideIdDTO): Observable<any>{
    const jwt_token = localStorage.getItem('jwt_token')
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${jwt_token}`
    })

    return this.http.post(`${this.apiUrl}/accept-ride`, ride_id_dto, {headers})
  }

  


  
}

import { HttpClient, HttpHeaderResponse, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LicenseIdDTO, TaxiLicenseRequestDTO } from '../../models/TaxiLicencesRequestDTO';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TaxiLicenseService {

  private apiUrl = "http://localhost:8000/api/taxi-license";
  constructor(private http: HttpClient) { }


  sendRequest(licence_request_dto: TaxiLicenseRequestDTO): Observable<any> {
    const jwt_token = localStorage.getItem('jwt_token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${jwt_token}`
    })

    return this.http.post(`${this.apiUrl}/send-license-request`, licence_request_dto, {headers})
  }

  getRequests() : Observable<any>{
     const jwt_token = localStorage.getItem('jwt_token');
     const headers = new HttpHeaders({
      'Authorization': `Bearer ${jwt_token}`
    })

    return this.http.get<any>(`${this.apiUrl}/get-license-requests`, {headers})
  }

  approve(licenseId:LicenseIdDTO): Observable<any> {
    const jwt_token = localStorage.getItem('jwt_token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${jwt_token}`
    })

    return this.http.post(`${this.apiUrl}/approve-driver`, licenseId, {headers})
  }
}

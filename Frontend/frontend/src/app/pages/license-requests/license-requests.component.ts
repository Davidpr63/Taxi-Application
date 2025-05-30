import { Component, OnInit } from '@angular/core';
import { LicenseDTO, LicenseIdDTO } from '../../models/TaxiLicencesRequestDTO';
import { CommonModule } from '@angular/common';
import { TaxiLicenseService } from '../../services/taxi-licence-service/taxi-licence.service';

@Component({
  selector: 'app-license-requests',
  imports: [CommonModule],
  templateUrl: './license-requests.component.html',
  styleUrl: './license-requests.component.scss'
})
export class LicenseRequestsComponent implements OnInit{

  licenseDTO: LicenseDTO []= []

  licenseId: LicenseIdDTO = {
    licenseId: ''
  }
  /**
   *
   */
  constructor(private taxiLicense: TaxiLicenseService) {}
  ngOnInit(): void {
    this.taxiLicense.getRequests().subscribe({
      next : (res) => {
        console.log(res.data)
        this.licenseDTO = res.data
      },
      error: (err) => {
        console.log("get license requests error", err)
      }
    })
  }

  approve(taxiLicenseId: string){
    this.licenseId.licenseId = taxiLicenseId
    console.log('license -> ', this.licenseId)
    this.taxiLicense.approve(this.licenseId).subscribe({
      next : (res) => {
        alert(res.message)
      },
      error: (err) => {
        console.log("handle requests error", err)
      }
    })
  }
}

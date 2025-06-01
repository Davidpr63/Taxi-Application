import { Component, OnInit } from '@angular/core';
import { LicenseDTO, LicenseIdDTO } from '../../models/TaxiLicencesRequestDTO';
import { CommonModule } from '@angular/common';
import { TaxiLicenseService } from '../../services/taxi-licence-service/taxi-licence.service';
import { ToastService } from '../../services/toast-service/toast.service';

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
  constructor(private taxiLicenseService: TaxiLicenseService, private toastrService: ToastService) {}
  ngOnInit(): void {
    this.taxiLicenseService.getRequests().subscribe({
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
    
    this.taxiLicenseService.approve(this.licenseId).subscribe({
      next : (res) => {
        if(res.message === 'success')
        {
          this.toastrService.success('You have successfully approved the request')

        }
        else
          this.toastrService.warning("You already approved the request")
      },
      error: (err) => {
        console.log("approve the request error", err)
      }
    })
  }
  reject(taxiLicenseId: string){
    this.licenseId.licenseId = taxiLicenseId;
    
    this.taxiLicenseService.reject(this.licenseId).subscribe({
      next : (res) => {
        if(res.message === 'success')
        {
          this.toastrService.success('You have successfully rejected the request')

        }
        else
          this.toastrService.warning("You have already rejected the request")
      },
      error: (err) => {
        console.log("reject the request error", err)
      }
    })
  }
}

import { Component } from '@angular/core';
import { TaxiLicenseRequestDTO } from '../../models/TaxiLicencesRequestDTO';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { TaxiLicenseService } from '../../services/taxi-licence-service/taxi-licence.service';
import { ToastService } from '../../services/toast-service/toast.service';

@Component({
  selector: 'app-get-taxi-licence',
  imports: [CommonModule, FormsModule],
  templateUrl: './get-taxi-licence.component.html',
  styleUrl: './get-taxi-licence.component.scss'
})
export class GetTaxiLicenceComponent {

  formError: string = '';
  licenseFormDto: TaxiLicenseRequestDTO = {
    car : '',
    licensePlate: '',
    email : ''
  }
  /**
   *
   */
  constructor(private taxiLicenseService: TaxiLicenseService, private toastrService : ToastService) {}
  sendRequest(){
    this.taxiLicenseService.sendRequest(this.licenseFormDto).subscribe({
      next : (res) => {
        if(res.message === "success")
          this.toastrService.success('The request has been sent successfully')
        else if(res.message === "failure")
          this.toastrService.warning('You have already sent the request')
      },
      error : (err) => {
        console.log('get-taxi-licence error')
      }
    })
  }
}

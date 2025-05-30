import { Component } from '@angular/core';
import { TaxiLicenseRequestDTO } from '../../models/TaxiLicencesRequestDTO';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { TaxiLicenseService } from '../../services/taxi-licence-service/taxi-licence.service';

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
  constructor(private taxiLicenseService: TaxiLicenseService) {}
  sendRequest(){
    this.taxiLicenseService.sendRequest(this.licenseFormDto).subscribe({
      next : (res) => {
        if(res.message === "success")
          alert("Request have sent successfully")
      },
      error : (err) => {
        console.log('get-taxi-licence error')
      }
    })
  }
}

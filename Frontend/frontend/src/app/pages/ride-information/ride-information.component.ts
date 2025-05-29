import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RideAcceptedDTO, RideInformationDTO } from '../../models/RideInformationDTO';
import { FormsModule } from '@angular/forms';
import { DriverService } from '../../services/driver-service/driver.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-ride-information',
  imports: [CommonModule, FormsModule],
  templateUrl: './ride-information.component.html',
  styleUrl: './ride-information.component.scss'
})
export class RideInformationComponent implements OnInit{
 

  ConfirmationError: string = ''
  ETA: number = 0
  

  RideAcceptedDTO: RideAcceptedDTO = {
    firstName : '',
    lastName : '',
    car : '',
    eta : 0
  }

  /**
   *
   */
  constructor(private driverService: DriverService, private router: Router) { }

  ngOnInit(): void {
   
  }

  notifyRideAccepted(){
    
    
    this.driverService.notifyRideAccepted(this.RideAcceptedDTO).subscribe({
      next : (res) => {
        if(res.message === 'success')
          alert('User have notified')
      },
      error : (err) => {
        console.log('notify ride accepted', err)
      }
    })
  }
}

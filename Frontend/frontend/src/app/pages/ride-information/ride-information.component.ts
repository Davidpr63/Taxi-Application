import { CommonModule } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { RideInformationDTO } from '../../models/RideInformationDTO';
import { FormsModule } from '@angular/forms';
import {  Router } from '@angular/router';
 


@Component({
  selector: 'app-ride-information',
  imports: [CommonModule, FormsModule],
  templateUrl: './ride-information.component.html',
  styleUrl: './ride-information.component.scss',
  standalone: true
})
export class RideInformationComponent{


  @Input() rideInfo: RideInformationDTO = {
    DriverFirstName: '',
    DriverLastName: '',
    DriverCar: '',
    ETA: 0
  };
  /**
   *
   */
  constructor(private router: Router) {
    
    
  }
  close(){
    this.router.navigate([""])
  }
  
}

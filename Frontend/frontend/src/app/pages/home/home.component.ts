import { CommonModule } from '@angular/common';
import { ChangeDetectorRef, Component} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RideRequestDTO } from '../../models/RideRequest';
import { HomeService } from '../../services/home-service/home.service';
import { Router } from '@angular/router';
import { RideRequestAnimationComponent } from "../../animations/ride-request-animation/ride-request-animation.component";
import { DriverService } from '../../services/driver-service/driver.service';
import {  RideInformationDTO } from '../../models/RideInformationDTO';



@Component({
  selector: 'app-home',
  imports: [CommonModule, FormsModule, RideRequestAnimationComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent  {
  
  formError: string = "";
  isLoading: boolean = false;
   
  
   RideInfoDTO: RideInformationDTO = {
      firstName: '',
      lastName: '',
      car: '',
      ETA: 0
    }
  rideRequest: RideRequestDTO = {
    pickupAddress: "",
    destinationAddress: ""
  }

  token = localStorage.getItem('jwt_token');
  /**
   *
   */
  constructor(private homeService: HomeService, private driverService: DriverService, private router: Router, private cdRef: ChangeDetectorRef) {}
   
   
  submit(){
    
    if(!this.token){
      this.formError = "You need to log in first.";
      return
    }

    this.isLoading = true;   
    this.homeService.sendRideRequest(this.rideRequest).subscribe({
      next: (res) => {
        if(res.message === "success"){
          this.homeService.getRideInfo().subscribe({
            next : (res) => {
              this.RideInfoDTO = res.data
              console.log(this.RideInfoDTO)
              this.isLoading = false;
            },
            error : (err) => {
              console.log("get ride info error:", err)
            }
          })
          
          
        }
        else{
          alert(res.message)
          this.isLoading = false;
        }
      },
      error: (error) => {

      }
    })
   
  }
}

import { CommonModule } from '@angular/common';
import { ChangeDetectorRef, Component, OnInit} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RideRequestDTO } from '../../models/RideRequest';
import { HomeService } from '../../services/home-service/home.service';
import { Router } from '@angular/router';
import { RideRequestAnimationComponent } from "../../animations/ride-request-animation/ride-request-animation.component";
import { DriverService } from '../../services/driver-service/driver.service';
import {  RideInformationDTO } from '../../models/RideInformationDTO';
import { RideInformationComponent } from '../ride-information/ride-information.component';
import { ToastService } from '../../services/toast-service/toast.service';
 



@Component({
  selector: 'app-home',
  imports: [CommonModule, FormsModule, RideRequestAnimationComponent, RideInformationComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent   {
  
  formError: string = "";
  isLoading: boolean = false;
   
  
   RideInfoDTO: RideInformationDTO = {
      DriverFirstName: '',
      DriverLastName: '',
      DriverCar: '',
      LicensePlate: '',
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
  constructor(private homeService: HomeService,private toastService: ToastService, private driverService: DriverService, private router: Router, private cdRef: ChangeDetectorRef) {}
    
   
   
  submit(){
    
    if(!this.token){
      this.formError = "Plaese log in first.";
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
              setTimeout(() => {
                this.RideInfoDTO.ETA = 0;
              }, 5000);
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
        console.log('send ride rquest error: ', error)
      }
    })
  
  }
 
}

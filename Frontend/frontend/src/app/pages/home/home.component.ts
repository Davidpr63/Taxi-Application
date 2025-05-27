import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RideRequestDTO } from '../../models/RideRequest';
import { HomeService } from '../../services/home-service/home.service';
import { Router } from '@angular/router';
import { RideRequestAnimationComponent } from "../../animations/ride-request-animation/ride-request-animation.component";

@Component({
  selector: 'app-home',
  imports: [CommonModule, FormsModule, RideRequestAnimationComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  
  formError: string = "";
  isLoading: boolean = false;


  rideRequest: RideRequestDTO = {
    pickupAddress: "",
    destinationAddress: ""
  }

  token = localStorage.getItem('jwt_token');
  /**
   *
   */
  constructor(private homeService: HomeService, private router: Router) {}

  submit(){
    
    if(!this.token){
      this.formError = "You need to log in first.";
      return
    }

    this.isLoading = true;
    this.homeService.rideRequest(this.rideRequest).subscribe({
      next: (res) => {
        if(res.message === "success"){
            console.log(res.message)
            alert(res.message)
            setTimeout(() => {

              this.isLoading = false;
              this.router.navigate([''])
            }, 2000)
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

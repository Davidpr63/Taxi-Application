import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RideIdDTO, RidesDTO } from '../../models/RidesDTO';
import { DriverService } from '../../services/driver-service/driver.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-ride-requests',
  imports: [CommonModule],
  templateUrl: './ride-requests.component.html',
  styleUrl: './ride-requests.component.scss'
})
export class RideRequestsComponent implements OnInit {


  rides: RidesDTO[] = [];
  rideIdDTO : RideIdDTO = {
    rideId : ''
  }
  constructor(private driverService: DriverService, private router: Router) {}

  ngOnInit(): void {
    this.driverService.getRideRequests().subscribe({
      next: (res) =>{
        this.rides = res
        console.log(this.rides)
      },
      error: (err) => {
        console.log("response getRideRequests error :", err)
      }
    })
  }
  acceptRide(rideId : string){
    console.log('ride -> ',rideId)
    this.rideIdDTO.rideId = rideId;
    this.driverService.acceptRide(this.rideIdDTO).subscribe({
      next: (res) => {
        if(res.message === "success")
          alert('success')
        else{
          alert(res.message)
        }
      },
      error: (err) => {
        console.log(err)
      }
    })
  }
}

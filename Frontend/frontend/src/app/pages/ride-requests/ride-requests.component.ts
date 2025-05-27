import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RidesDTO } from '../../models/RidesDTO';
import { DriverService } from '../../services/driver-service/driver.service';

@Component({
  selector: 'app-ride-requests',
  imports: [CommonModule],
  templateUrl: './ride-requests.component.html',
  styleUrl: './ride-requests.component.scss'
})
export class RideRequestsComponent implements OnInit {


  rides: RidesDTO[] = [];
  
  constructor(private driverService: DriverService) {}

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

  }
}

import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RideIdDTO, RidesDTO } from '../../models/RidesDTO';
import { DriverService } from '../../services/driver-service/driver.service';
import { Router } from '@angular/router';
import { ToastService } from '../../services/toast-service/toast.service';

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
  constructor(private driverService: DriverService, private router: Router, private toastrService: ToastService) {}

  ngOnInit(): void {
    this.driverService.getRideRequests().subscribe({
      next: (res) =>{
        this.rides = res
        
      },
      error: (err) => {
        console.log("response getRideRequests error :", err)
      }
    })
  }
  acceptRide(rideId : string){
    
    this.rideIdDTO.rideId = rideId;
    this.driverService.acceptRide(this.rideIdDTO).subscribe({
      next: (res) => {
        if(res.message === "success")
          this.toastrService.success('You have successfully accepted a ride. You can start driving')
        else{
          this.toastrService.info('Cannot accept the ride because it has already been accepted.')
        }
      },
      error: (err) => {
        console.log(err)
      }
    })
  }
}

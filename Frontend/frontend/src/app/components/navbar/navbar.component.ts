import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth-service/auth.service';
import { CommonModule } from '@angular/common';
import { BehaviorSubject, Observable } from 'rxjs';
 

@Component({
  selector: 'app-navbar',
  imports: [CommonModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent implements OnInit{
  
  isLoggedIn: boolean = false;
  userRole: string | null= 'user';
  constructor(private router: Router, private auth_service: AuthService) {
   
  }
  ngOnInit(): void {
    this.auth_service.isLoggedIn$.subscribe(value => {
    this.isLoggedIn = value;
  });

  this.auth_service.userRole$.subscribe(role => {
    this.userRole = role;
  });
  console.log(this.isLoggedIn, this.userRole)
  }
  
  logout(){
    this.auth_service.logout();
  }

}

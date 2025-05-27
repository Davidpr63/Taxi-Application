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
export class NavbarComponent {
  
  isLoggedIn$: Observable<boolean>;
  userRole$: Observable<string | null>;
  constructor(private router: Router, private auth_service: AuthService) {
    this.isLoggedIn$ = this.auth_service.isLoggedIn$;
    this.userRole$ = this.auth_service.userRole$;
  }
  
  logout(){
    this.auth_service.logout();
  }

}

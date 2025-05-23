import { Component, NgModule } from '@angular/core';
import { RegisterUserDTO } from '../../models/UserDTO';
import { AuthService } from '../../services/auth-service/auth.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registration',
  imports: [FormsModule, CommonModule],
  templateUrl: './registration.component.html',
  styleUrl: './registration.component.scss'
})
export class RegistrationComponent {
 
  registrationError: string = "";

  user: RegisterUserDTO = {
    first_name: "",
    last_name: "",
    username: "",
    password: "",
    confirm_password: "",
    phone_number: "",  
  }
 
  constructor(private authService: AuthService, private router: Router) { }

  registration(){
    if(!this.user.first_name || !this.user.last_name || !this.user.username || !this.user.password || !this.user.confirm_password || !this.user.phone_number) {
      alert("All fields have to fill out");
      return;
    }
    this.authService.register(this.user).subscribe({
      next: (res) => {
        if(res.message === "success"){
          alert(res.message)
          this.registrationError = "";
          this.router.navigate(['/login']);
        }
          
        else
          this.registrationError = res.message
      },
      error: (err) => alert("error occured while regiter user" + err.error?.error),
    })
  }
}

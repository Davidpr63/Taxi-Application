import { Component } from '@angular/core';
import { LoginUserDTO } from '../../models/UserDTO';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-login',
  imports: [FormsModule, CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {

  loginError: string = "";

  loginUserDto : LoginUserDTO = {
    username: "",
    password: ""
  }

  /**
   *
   */
  constructor(private auth_service: AuthService, private router: Router) { }

  login(){
    if(!this.loginUserDto.username || !this.loginUserDto.password){
      alert("Please fill out all fields")
      return;
    }
    this.auth_service.login(this.loginUserDto).subscribe({
      next: (res) => {
        if(res.message === "success"){
          
          this.auth_service.saveToken(res.jwt_token)
          
          this.router.navigate([""])
        }
        else
            this.loginError = res.message;
            
      },
      error: (err) => {
      console.error('Error during login', err);
      
    }
    })

  }

  

}

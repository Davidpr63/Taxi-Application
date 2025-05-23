import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { UserProfileDTO } from '../../models/UserDTO';
import { FormsModule } from '@angular/forms';
import { UserService } from '../../services/user-service/user-service.service';

@Component({
  selector: 'app-edit-profile',
  imports: [CommonModule, FormsModule],
  templateUrl: './edit-profile.component.html',
  styleUrl: './edit-profile.component.scss'
})
export class EditProfileComponent implements OnInit {

  EditError: string = "";

  user: UserProfileDTO = {
    first_name : "",
    last_name : "",
    username : "",
    phone_number: ""
  }
  
  newUserDataDTO = {
    first_name : "",
    last_name : "",
    username : "",
    password: "",
    confirm_password: "",
    phone_number: ""
  }
  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.userService.GetUserData().subscribe({
      next: data => {
         
        this.user = data;
         
      },
      error : err => {
        console.error("An error was occurred while fetching data for user", err);
      }
    });
  }

  update(){
    
    this.newUserDataDTO.first_name = this.user.first_name;
    this.newUserDataDTO.last_name = this.user.last_name;
    this.newUserDataDTO.username = this.user.username;
    this.newUserDataDTO.phone_number = this.user.phone_number;
    
    this.userService.updateUserData(this.newUserDataDTO).subscribe({
      next: (data) => {
        if(data.message === "success"){
          alert("Data have successfuly updated")
          this.EditError = "";
        }
          

        else
          this.EditError = data.message;
      },
      error: (err) =>{
        console.error('Error updating', err);
      }
    })
  }
}

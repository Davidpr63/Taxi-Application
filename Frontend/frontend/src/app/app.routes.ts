import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { RegistrationComponent } from './pages/registration/registration.component';
import { LoginComponent } from './pages/login/login.component';


export const routes: Routes = [

   {
        path: '',
        pathMatch:'full',
        loadComponent() {
            return import('./pages/home/home.component').then((x) => x.HomeComponent)
        },
   },
   {
        path: 'registration',
        loadComponent() {
            return import('./pages/registration/registration.component').then((x) => x.RegistrationComponent)
        },
   },
   {
        path: 'login',
        loadComponent() {
            return import('./pages/login/login.component').then((x) => x.LoginComponent)
        },
   },
   {
        path: 'my-profile',
        loadComponent() {
            return import('./pages/edit-user-profile/edit-profile.component').then((x) => x.EditProfileComponent)
        },
   }
];

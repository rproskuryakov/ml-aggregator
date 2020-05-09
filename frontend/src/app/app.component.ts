import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <mat-toolbar color="primary" class="mat-elevation-z10">
      <button mat-button>Online Exams</button>
      <button mat-button>About</button>

      <!-- This fills the remaining space of the current row -->
      <span class="fill-remaining-space"></span>

      <!-- <button mat-button (click)="signIn()" *ngIf="!authenticated">Sign In</button> -->
      <!-- <button mat-button (click)="signOut()" *ngIf="authenticated">Sign Out</button> -->
    </mat-toolbar>

<div class="view-container">
  <router-outlet></router-outlet>
</div>

  `,
  styleUrls: ['./app.component.css']
})
export class AppComponent { }

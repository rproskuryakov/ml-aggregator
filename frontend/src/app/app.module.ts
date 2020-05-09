import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { ExamsApiService } from './exams/exams-api.service';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { ExamFormComponent } from './exams/exam-form.component';
import { RouterModule, Routes } from '@angular/router';
import { ExamsComponent } from './exams/exams.component';

import {NoopAnimationsModule} from '@angular/platform-browser/animations';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';


const appRoutes: Routes = [
  { path: 'new-exam', component: ExamFormComponent },
  { path: '', component: ExamsComponent },
];



@NgModule({
  declarations: [
    AppComponent,
    ExamFormComponent,
    ExamsComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(
      appRoutes,
    ),
    NoopAnimationsModule,
    MatButtonModule,
    MatToolbarModule,
    MatCardModule,
    MatInputModule,
  ],
  providers: [ExamsApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}

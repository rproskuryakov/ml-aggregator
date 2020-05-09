import {Component, OnDestroy, OnInit} from '@angular/core';
import {SubscriptionLike} from 'rxjs';
import {Exam} from './exam.model';
import {ExamsApiService} from './exams-api.service';

@Component({
  selector: 'exams',
  template: `
    <h2>Exams</h2>
    <p>Choose an exam and start studying.</p>
    <div class="exams">
      <mat-card class="example-card" *ngFor="let exam of examsList" class="mat-elevation-z5">
        <mat-card-content>
          <mat-card-title>{{exam.title}}</mat-card-title>
          <mat-card-subtitle>{{exam.description}}</mat-card-subtitle>
          <p>
            {{exam.long_description}}
          </p>
          <button mat-raised-button color="accent">Start Exam</button>
        </mat-card-content>
      </mat-card>
    </div>
    <button mat-fab color="primary"
            class="new-exam" routerLink="/new-exam">
      <i class="material-icons">note_add</i>
    </button>
  `,
  styleUrls: ['exams.component.css'],
})
export class ExamsComponent implements OnInit, OnDestroy {
  examsListSubs: SubscriptionLike;
  examsList: Exam[];

  constructor(private examsApi: ExamsApiService) {
  }

  ngOnInit() {
    this.examsListSubs = this.examsApi
      .getExams()
      .subscribe(res => {
          this.examsList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.examsListSubs.unsubscribe();
  }
}

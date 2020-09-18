import {Component, OnDestroy, OnInit} from '@angular/core';
import {SubscriptionLike} from 'rxjs';
import {Article} from './article.model';
import {ArticlesApiService} from './articles-api.service';

@Component({
  selector: 'articles',
  template: `
    <h2>Articles</h2>
    <p>Here we are!</p>
    <div class="articles">
      <mat-card class="example-card" *ngFor="let article of articlesList" class="mat-elevation-z5">
        <mat-card-content>
          <mat-card-title> <a href="{{article.articleUrl}}">{{article.name}}</a></mat-card-title>
          <mat-card-subtitle>{{article.source}}</mat-card-subtitle>
          <p>
            {{article.summary}}
          </p>
          <!--- <app-favourite-button></app-favourite-button> --->
        </mat-card-content>
      </mat-card>
    </div>
  `,
  styleUrls: ['articles.component.css'],
})
export class ArticlesComponent implements OnInit, OnDestroy {
  articlesListSubs: SubscriptionLike;
  articlesList: Article[];

  constructor(private articlesApi: ArticlesApiService) {
  }

  ngOnInit() {
    this.articlesListSubs = this.articlesApi
      .getArticles()
      .subscribe(res => {
          this.articlesList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.articlesListSubs.unsubscribe();
  }
}

import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse }from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../env';
import { Article } from './article.model';

@Injectable()
export class ArticlesApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getArticles(): Observable<Article[]> {
    return this.http
      .get<Article[]>(`${API_URL}/articles`)
      .pipe(
      catchError(ArticlesApiService._handleError)
      );
  }

  saveArticle(article: Article): Observable<any> {
    return this.http
      .post(`${API_URL}/articles`, article);
  }
}

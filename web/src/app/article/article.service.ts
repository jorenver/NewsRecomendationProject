import { HttpClient, HttpParams } from '@angular/common/http'
import { Injectable } from '@angular/core';
import { Article } from './article';
import { Observable } from 'rxjs';
import { SelectionOption } from '../shared/selection-option';

@Injectable({ providedIn: 'root' })
export class ArticleService {
  private readonly urlBase = 'http://127.0.0.1:5000'

  constructor(private readonly http: HttpClient) {}

  getCategories():Observable<Array<string>> {
    console.log(`getCategories`)
    return this.http.get<Array<string>>(`${this.urlBase}/categories`)
  }

  getArticles(category: string):Observable<Array<Article>> {
    console.log(`getArticles: ${category}`)
    const params = new HttpParams().append("category", category)

    return this.http.get<Array<Article>>(`${this.urlBase}/articles`, { params: params })
  }
}

import { Component } from '@angular/core';
import { SelectionOption } from './shared/selection-option';
import { Article } from './article/article';
import { ArticleService } from './article/article.service';
import { MatDialog } from '@angular/material/dialog';
import { CollectorProccesDialogComponent } from './dialog/collector-procces-dialog/collector-procces-dialog.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  label = 'Category'

  categories: Array<string> = []

  articles: Array<Article> = []

  constructor(
    private readonly articleService: ArticleService,
    private readonly dialog: MatDialog) {
    this.loadCategories()
  }

  private loadCategories(): void {
    this.articleService.getCategories()
      .subscribe(response => {
        console.log(response)
        this.categories = response
      })
  }

  changeCategory(value: string): void {
    console.log('changeCategory')
    this.articleService.getArticles(value)
      .subscribe(response => {
        console.log(response)
        this.articles = response
      })
  }

  showCollectorProcessDialog(): void {
    this.dialog
      .open(CollectorProccesDialogComponent, {
        panelClass: ['gc-dialog-panel--xs'],
        autoFocus: false
      })
      .afterClosed()
      .subscribe((accept: boolean) => {
        console.log(accept)
      })
  }
}

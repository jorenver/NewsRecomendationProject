export class Article {
  author: string = ''
  title: string = ''
  description: string = ''
  url: string = ''
  urlToImage: string = ''

  constructor(fields?: Partial<Article>) {
    if (fields) {
      Object.assign(this, fields)
    }
  }
}

export class SelectionOption {
  value: string = ''
  description: string = ''

  constructor(fields?: Partial<SelectionOption>) {
    if (fields) {
      Object.assign(this, fields)
    }
  }
}

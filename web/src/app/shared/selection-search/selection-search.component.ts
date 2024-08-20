import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { SelectionOption } from '../selection-option';
import { MatSelectChange } from '@angular/material/select';

@Component({
  selector: 'app-selection-search',
  templateUrl: './selection-search.component.html',
  styleUrls: ['./selection-search.component.scss']
})
export class SelectionSearchComponent {
  @Input()
  label: string = ''

  @Input()
  options: Array<string> = []

  @Output()
  readonly onSelectionChange = new EventEmitter<string>()

  selectOption(event: MatSelectChange): void {
    this.onSelectionChange.emit(event.value)
  }

}

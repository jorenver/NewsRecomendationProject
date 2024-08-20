import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CollectorProccesDialogComponent } from './collector-procces-dialog.component';

describe('CollectorProccesDialogComponent', () => {
  let component: CollectorProccesDialogComponent;
  let fixture: ComponentFixture<CollectorProccesDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CollectorProccesDialogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CollectorProccesDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

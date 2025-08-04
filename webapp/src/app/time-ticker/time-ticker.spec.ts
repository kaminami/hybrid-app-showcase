import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TimeTicker } from './time-ticker';

describe('TimeTicker', () => {
  let component: TimeTicker;
  let fixture: ComponentFixture<TimeTicker>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TimeTicker]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TimeTicker);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

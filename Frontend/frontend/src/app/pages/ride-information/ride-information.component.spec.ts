import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RideInformationComponent } from './ride-information.component';

describe('RideInformationComponent', () => {
  let component: RideInformationComponent;
  let fixture: ComponentFixture<RideInformationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RideInformationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RideInformationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

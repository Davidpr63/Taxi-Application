import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RideRequestInfoComponent } from './ride-request-info.component';

describe('RideRequestInfoComponent', () => {
  let component: RideRequestInfoComponent;
  let fixture: ComponentFixture<RideRequestInfoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RideRequestInfoComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RideRequestInfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

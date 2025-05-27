import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RideRequestAnimationComponent } from './ride-request-animation.component';

describe('RideRequestAnimationComponent', () => {
  let component: RideRequestAnimationComponent;
  let fixture: ComponentFixture<RideRequestAnimationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RideRequestAnimationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RideRequestAnimationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

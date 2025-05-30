import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetTaxiLicenceComponent } from './get-taxi-licence.component';

describe('GetTaxiLicenceComponent', () => {
  let component: GetTaxiLicenceComponent;
  let fixture: ComponentFixture<GetTaxiLicenceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GetTaxiLicenceComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GetTaxiLicenceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

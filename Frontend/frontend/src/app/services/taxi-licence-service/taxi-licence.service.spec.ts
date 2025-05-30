import { TestBed } from '@angular/core/testing';

import { TaxiLicenceService } from './taxi-licence.service';

describe('TaxiLicenceService', () => {
  let service: TaxiLicenceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TaxiLicenceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

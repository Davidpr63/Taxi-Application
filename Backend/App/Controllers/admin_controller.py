from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import JSONResponse

from Backend.App.Core.dependencies import get_taxi_licence_service
from Backend.App.DtoModels.license_id import LicenseIdDTO
from Backend.App.DtoModels.license_request_dto import TaxiLicenseRequestDTO
from Backend.App.Utils.Jwt import jwt_config

router = APIRouter(prefix="/api/taxi-license")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/send-license-request")
def accept_licence_request(licence_request_dto: TaxiLicenseRequestDTO, token: str = Depends(oauth2_scheme), taxi_licence_service = Depends(get_taxi_licence_service)):
    try:
        print(licence_request_dto)
        user_row_key = jwt_config.get_row_key_from_token(token)
        result = taxi_licence_service.handle_request(user_row_key, licence_request_dto)
        return JSONResponse(content={'message':result})
    except Exception as e:
        print(e)

@router.get("/get-license-requests")
def get_license_request(token: str = Depends(oauth2_scheme), taxi_license_service = Depends(get_taxi_licence_service)):
    try:
        result = taxi_license_service.get_license_requests()
        return JSONResponse(content={"data":result})
    except Exception as e:
        print(e)

@router.post("/approve-license-request")
def approve_driver(license_id : LicenseIdDTO, token: str = Depends(oauth2_scheme), taxi_license_service = Depends(get_taxi_licence_service)):
    try:

        result = taxi_license_service.approve_request(license_id.licenseId)

        return JSONResponse(content={"message":result})
    except Exception as e:
        print(e)


@router.post("/reject-license-request")
def approve_driver(license_id : LicenseIdDTO, token: str = Depends(oauth2_scheme), taxi_license_service = Depends(get_taxi_licence_service)):
    try:

        result = taxi_license_service.reject_request(license_id.licenseId)

        return JSONResponse(content={"message":result})
    except Exception as e:
        print(e)
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import JSONResponse

from Backend.App.Core.dependencies import get_driver_service
from Backend.App.DtoModels.ride_id_dto import RideIdDTO
from Backend.App.Utils.Jwt import jwt_config

router = APIRouter(prefix="/api/driver")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/get-ride-requests")
def ride_requests(token:str = Depends(oauth2_scheme), driver_service = Depends(get_driver_service)):
    try:
        result = driver_service.get_all_requests()
        return JSONResponse(result)
    except Exception as e:
        print(e)

@router.post("/accept-ride")
def accept_ride(ride_id_dto: RideIdDTO , token:str = Depends(oauth2_scheme), driver_service = Depends(get_driver_service)):
    try:
        print('ride row key', ride_id_dto.rideId)
        driver_row_key = jwt_config.get_row_key_from_token(token)
        result = driver_service.accept_ride(ride_id_dto.rideId, driver_row_key)
        return JSONResponse(content={"message": result})
    except Exception as e:
        print(e)


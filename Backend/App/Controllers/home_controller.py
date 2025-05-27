from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import JSONResponse

from Backend.App.Core.dependencies import get_home_service
from Backend.App.DtoModels.ride_request_dto import RideRequestDTO
from Backend.App.Utils.Jwt import jwt_config

router = APIRouter(prefix="/api/home")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/ride-request")
def ride_request(ride_request_dto: RideRequestDTO, token:str = Depends(oauth2_scheme), home_service = Depends(get_home_service)):
    try:
        print(ride_request_dto)

        user_row_key = jwt_config.get_row_key_from_token(token)

        if user_row_key == "invalid token":
            return JSONResponse(content={"message":"Before requesting a ride, first log in"})

        result = home_service.handle_ride_request(ride_request_dto, user_row_key)

        return JSONResponse(content={"message":"success"})
    except Exception as e:
        print(e)
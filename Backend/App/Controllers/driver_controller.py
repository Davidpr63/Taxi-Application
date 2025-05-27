from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import JSONResponse

from Backend.App.Core.dependencies import get_driver_service

router = APIRouter(prefix="/api/driver")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/get-ride-requests")
def ride_requests(token:str = Depends(oauth2_scheme), driver_service = Depends(get_driver_service)):
    try:
        result = driver_service.get_all_requests()
        return JSONResponse(result)
    except Exception as e:
        print(e)
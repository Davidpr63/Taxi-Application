from traceback import print_tb

from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import JSONResponse
from Backend.App.Core.dependencies import get_user_service
from Backend.App.DtoModels.new_user_data import NewUserDataDTO
from Backend.App.DtoModels.user_profile_dto import UserProfileDTO
from Backend.App.Utils.Jwt import jwt_config

router = APIRouter(prefix="/api/user")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/my-profile")
def user_profile(token: str = Depends(oauth2_scheme), user_service = Depends(get_user_service)):
    try:
        print(token)
        row_key = jwt_config.get_row_key_from_token(token)
        print(row_key)
        user_profile_dto = user_service.get_user_data(row_key)
        return JSONResponse(user_profile_dto)
    except Exception as e:
        print(e)

@router.post("/update-user")
def update_user(new_user_data_dto: NewUserDataDTO, token: str = Depends(oauth2_scheme), user_service = Depends(get_user_service)):
    try:
        print(new_user_data_dto)
        row_key = jwt_config.get_row_key_from_token(token)
        result = user_service.update_user_data(row_key, new_user_data_dto)
        return JSONResponse(content={"message":result})
    except Exception as e:
        print(e)
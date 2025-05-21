from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from Backend.App.Core.dependencies import get_auth_service
from Backend.App.DtoModels.LoginUserDTO import LoginUserDTO
from Backend.App.DtoModels.userDTO import RegisterUserDTO

router = APIRouter(prefix="/api/auth")


@router.post("/registration")
def registration(user_dto: RegisterUserDTO, auth_service=Depends(get_auth_service)):
    try:
        print(user_dto)
        result = auth_service.register(user_dto)

        return JSONResponse(content={"message": result})
    except Exception as e:
        print('[Controller] An error was occurred during registration : ', e)


@router.post("/login")
def login(login_dto: LoginUserDTO, auth_service = Depends(get_auth_service)):
    try:
        print(login_dto)
        result = auth_service.login(login_dto)

        return JSONResponse(content={"message": result['result'], "jwt_token": result['jwt']})
    except Exception as e:
        print('[Controller] An error was occurred during logging : ', e)


from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from Backend.App.Controllers import auth_controller, user_controller, home_controller, driver_controller, \
    admin_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
def test():
    return "radi"
app.include_router(auth_controller.router)
app.include_router(user_controller.router)
app.include_router(home_controller.router)
app.include_router(driver_controller.router)
app.include_router(admin_controller.router)


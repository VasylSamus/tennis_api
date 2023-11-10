from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from routers.auth import auth_router
from routers.enum import enum_router
from routers.main import main_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount("/auth", app_auth)
app.include_router(auth_router, prefix='/api/auth', tags=['Auth'])
app.include_router(enum_router, prefix='/api/enum', tags=['Enum'])
app.include_router(main_router, prefix='/api')


@app.get("/")
async def root():
    return RedirectResponse(url='/docs')


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

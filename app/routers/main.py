from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_session
from models.main import *
from pydantic_models.main import *


main_router = APIRouter()


@main_router.get("/countries", tags=["Country"], status_code=200)
def get_countries(
        db_session: Annotated[Session, Depends(get_session)]
):
    return db_session.query(CountryDBModel).all()


@main_router.post("/countries", tags=["Country"], status_code=201)
def get_countries(
        country: CountryBase,
        db_session: Annotated[Session, Depends(get_session)]
):
    db_country = CountryDBModel(**dict(country))
    db_session.add(db_country)
    db_session.commit()
    return db_country


@main_router.get("/cities", tags=["City"], status_code=200)
def get_cities(
        db_session: Annotated[Session, Depends(get_session)]
):
    return db_session.query(CityDBModel).all()


# @main_router.post("/cities",  tags=["City"], status_code=201)
# def create_city(
#         city: CityDBModel,
#         db_session: Annotated[Session, Depends(get_session)]
# ):
#     pass

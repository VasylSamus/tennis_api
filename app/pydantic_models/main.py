from typing import Optional

from pydantic import BaseModel, Field


class Games(BaseModel):
    id: int
    name: str
    active: bool


class CountryBase(BaseModel):
    iso_code: Optional[str] = Field(None, max_length=3)
    name: str = Field(None, max_length=255)
    name_en: Optional[str] = Field(None, max_length=255)


class Country(CountryBase):
    id: int
    image: Optional[str] = Field(None, max_length=255)


class City(BaseModel):
    ...

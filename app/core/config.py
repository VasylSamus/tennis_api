from typing import ClassVar, List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str = 'tennis_su'
    POSTGRES_HOST: str = '127.0.0.1'
    POSTGRES_PASSWORD: str = 'Cvjhjlbyf1'
    POSTGRES_DB: str = 'tennis_db'
    POSTGRES_PORT: str = '5439'
    PG_URL: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    DATABASE_URL: str = ''
    DB_DICT: dict = {}

    LOG_LEVEL: str = "INFO"
    DEBUG: bool = True

    LOG_CONFIG: ClassVar = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {"default": {"format": "%(asctime)s [%(process)s] %(levelname)s: %(message)s"}},
        "handlers": {
            "console": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "level": LOG_LEVEL,
            }
        },
        "root": {"handlers": ["console"], "level": LOG_LEVEL},
        "loggers": {
            "gunicorn": {"propagate": True},
            "gunicorn.access": {"propagate": True},
            "gunicorn.error": {"propagate": True},
            "uvicorn": {"propagate": True},
            "uvicorn.access": {"propagate": True},
            "uvicorn.error": {"propagate": True},
            "sqlalchemy.engine": {"propagate": True},
        },
    }

    class Config:
        case_sensitive = True
        env_file = "../../.env"
        env_file_encoding = "utf-8"


settings = Settings()
# settings.DATABASE_URL = (f"postgresql://{settings.POSTGRES_USER}:{settings:POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}")
#
# settings.DB_DICT = dict(
#     host=settings.POSTGRES_HOST,
#     port=int(settings.POSTGRES_PORT),
#     user=settings.POSTGRES_USER,
#     password=settings.POSTGRES_PASSWORD,
#     database=settings.POSTGRES_DB
# )


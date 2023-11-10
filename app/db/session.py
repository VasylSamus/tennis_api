from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

# engine = create_engine(
#     f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}"
#     f"@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}"
# )

SQLALCHEMY_DATABASE_URL = settings.PG_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

sync_session = sessionmaker(bind=engine, class_=Session, expire_on_commit=False, )


class Base(DeclarativeBase):
    pass


# @contextmanager
def get_session() -> Session:
    db = sync_session()
    try:
        yield db
    finally:
        db.close()

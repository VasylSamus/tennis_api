from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.common import CreateUpdateDate
from db import Base
from models.main import PersonDBModel, PlayerDBModel



    # player: Mapped["PlayerDBModel"] = relationship(back_populates="person", uselist=False)




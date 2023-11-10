import datetime

from sqlalchemy import String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


from db import Base
from models.common import CreateUpdateDate
from pydantic_models.enum import (BackhandTypeEnum, HandEnum, MatchTypeEnum, GenderEnum, SurfaceTypeEnum,
                                 TournamentStageTypeEnum)


class UserDBModel(Base, CreateUpdateDate):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default='false')
    person_id: Mapped[int] = mapped_column(ForeignKey("persons.id"), nullable=True)
    person: Mapped["PersonDBModel"] = relationship(back_populates="user", uselist=False)


class GameDBModel(Base, CreateUpdateDate):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)


class PersonDBModel(Base, CreateUpdateDate):
    __tablename__ = 'persons'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    phone: Mapped[str] = mapped_column(String(255), nullable=True)
    address: Mapped[str] = mapped_column(String(255), nullable=True)
    gender: Mapped[GenderEnum] = mapped_column(Enum(GenderEnum), nullable=False, default=GenderEnum.MALE)
    player: Mapped["PlayerDBModel"] = relationship(back_populates="person", uselist=False)
    user: Mapped["UserDBModel"] = relationship(back_populates="person", uselist=False)


class PlayerDBModel(Base, CreateUpdateDate):
    __tablename__ = 'players'

    id: Mapped[int] = mapped_column(primary_key=True)
    person_id: Mapped[int] = mapped_column(ForeignKey("persons.id"))
    person: Mapped["PersonDBModel"] = relationship(back_populates="player", uselist=False)
    hand: Mapped[HandEnum] = mapped_column(Enum(HandEnum), nullable=False, default=HandEnum.RIGHT)
    backhand_type: Mapped[BackhandTypeEnum] = mapped_column(Enum(BackhandTypeEnum),
                                                            nullable=False, default=BackhandTypeEnum.TWO_HAND)
    tournament_player_ranks = relationship("TournamentPlayerRankDBModel", back_populates="player")


class CountryDBModel(Base, CreateUpdateDate):
    __tablename__ = 'countries'

    id: Mapped[int] = mapped_column(primary_key=True)
    iso_code: Mapped[str] = mapped_column(String(3), unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    name_en: Mapped[str] = mapped_column(String(255), nullable=False)
    image: Mapped[str] = mapped_column(String(255), nullable=True)
    cities: Mapped["CityDBModel"] = relationship(back_populates="country")


class CityDBModel(Base, CreateUpdateDate):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    country: Mapped["CountryDBModel"] = relationship(back_populates="cities")
    stadiums: Mapped["StadiumDBModel"] = relationship(back_populates="city")


class StadiumDBModel(Base, CreateUpdateDate):
    __tablename__ = 'stadiums'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    surface_type: Mapped[SurfaceTypeEnum] = mapped_column(Enum(SurfaceTypeEnum),
                                                          nullable=False, default=SurfaceTypeEnum.CLAY)
    courts_count: Mapped[int] = mapped_column(nullable=False, default=1)
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    city: Mapped["CityDBModel"] = relationship(back_populates="stadiums")
    address: Mapped[str] = mapped_column(String(500), nullable=True)
    phone: Mapped[str] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    info: Mapped[str] = mapped_column(Text, nullable=True)
    manager_id: Mapped[int] = mapped_column(ForeignKey("persons.id"))
    manager: Mapped["PersonDBModel"] = relationship(uselist=False)
    tournaments: Mapped["TournamentDBModel"] = relationship(back_populates="stadium")


class TournamentSettingsDBModel(Base, CreateUpdateDate):
    __tablename__ = 'tournament_settings'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    match_type: Mapped[MatchTypeEnum] = mapped_column(Enum(MatchTypeEnum), nullable=False, default=MatchTypeEnum.SINGLE)
    sets: Mapped[int] = mapped_column(nullable=False, default=2)
    games: Mapped[int] = mapped_column(nullable=False, default=6)
    gender: Mapped[GenderEnum] = mapped_column(Enum(GenderEnum), nullable=True)
    basket_sum_min: Mapped[int] = mapped_column(nullable=False, default=3)
    tournaments:  Mapped["TournamentDBModel"] = relationship(back_populates="tournament_settings")


class TournamentDBModel(Base, CreateUpdateDate):
    __tablename__ = 'tournaments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    date_to: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    info: Mapped[str] = mapped_column(Text, nullable=True)
    tournament_settings_id: Mapped[int] = mapped_column(ForeignKey("tournament_settings.id"), nullable=True)
    tournament_settings: Mapped["TournamentSettingsDBModel"] = relationship(back_populates="tournaments")
    stadium_id: Mapped[int] = mapped_column(ForeignKey("stadiums.id"), nullable=True)
    stadium: Mapped["StadiumDBModel"] = relationship(back_populates="tournaments")
    tournament_groups: Mapped["TournamentStageDBModel"] = relationship(back_populates="tournament")
    tournament_player_ranks: Mapped["TournamentPlayerRankDBModel"] = relationship(back_populates="tournament")


class TournamentStageDBModel(Base, CreateUpdateDate):
    __tablename__ = 'tournament_stages'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, default="Group")
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournaments.id"))
    tournament: Mapped["TournamentDBModel"] = relationship(back_populates="tournament_groups")
    stage_type: Mapped[TournamentStageTypeEnum] = mapped_column(Enum(TournamentStageTypeEnum),
                                                                nullable=False, default=TournamentStageTypeEnum.GROUP)
    matches: Mapped["MatchDBModel"] = relationship(back_populates="tournament_stage")


class TournamentPlayerDBModel(Base, CreateUpdateDate):
    __tablename__ = 'tournament_players'

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"))
    player: Mapped["PlayerDBModel"] = relationship()
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournaments.id"))
    tournament: Mapped["TournamentDBModel"] = relationship()


class TournamentStagePlayerDBModel(Base, CreateUpdateDate):
    __tablename__ = 'tournament_stage_players'

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"))
    player: Mapped["PlayerDBModel"] = relationship()
    tournament_stage_id: Mapped[int] = mapped_column(ForeignKey("tournament_stages.id"))
    tournament_stage: Mapped["TournamentStageDBModel"] = relationship()


class MatchDBModel(Base, CreateUpdateDate):
    __tablename__ = 'matches'

    id: Mapped[int] = mapped_column(primary_key=True)
    player11_id: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=True)
    player11: Mapped["PlayerDBModel"] = relationship(foreign_keys=[player11_id])
    player12_id: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=True)
    player12: Mapped["PlayerDBModel"] = relationship(foreign_keys=[player12_id])
    player21_id: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=True)
    player21: Mapped["PlayerDBModel"] = relationship(foreign_keys=[player21_id])
    player22_id: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=True)
    player22: Mapped["PlayerDBModel"] = relationship(foreign_keys=[player22_id])
    result: Mapped[str] = mapped_column(String(255), nullable=True)
    date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True, default=datetime.datetime.now())
    tournament_stage_id: Mapped[int] = mapped_column(ForeignKey("tournament_stages.id"), nullable=True)
    tournament_stage: Mapped["TournamentStageDBModel"] = relationship(back_populates="matches")
    match_source1_id: Mapped[int] = mapped_column(ForeignKey("matches.id"), nullable=True)
    match_source1: Mapped["MatchDBModel"] = relationship(foreign_keys=[match_source1_id])
    match_source2_id: Mapped[int] = mapped_column(ForeignKey("matches.id"), nullable=True)
    match_source2: Mapped["MatchDBModel"] = relationship(foreign_keys=[match_source2_id])
    is_ranking: Mapped[bool] = mapped_column(default=False, server_default='false')
    winner: Mapped[int] = mapped_column(nullable=True)
    sets1: Mapped[int] = mapped_column(nullable=True, default=0)
    sets2: Mapped[int] = mapped_column(nullable=True, default=0)
    games1: Mapped[int] = mapped_column(nullable=True, default=0)
    games2: Mapped[int] = mapped_column(nullable=True, default=0)
    stadium_id: Mapped[int] = mapped_column(ForeignKey("stadiums.id"), nullable=True)
    stadium:  Mapped["StadiumDBModel"] = relationship()
    info: Mapped[str] = mapped_column(Text, nullable=True)


class TournamentPlayerRankDBModel(Base, CreateUpdateDate):
    __tablename__ = 'tournament_player_ranks'

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"))
    player: Mapped["PlayerDBModel"] = relationship(back_populates="tournament_player_ranks")
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournaments.id"))
    tournament: Mapped["TournamentDBModel"] = relationship(back_populates="tournament_player_ranks")
    rank: Mapped[int] = mapped_column(nullable=False, default=0)
    points: Mapped[int] = mapped_column(nullable=False, default=0)
    matches_played: Mapped[int] = mapped_column(nullable=False, default=0)
    matches_won: Mapped[int] = mapped_column(nullable=False, default=0)
    matches_lost: Mapped[int] = mapped_column(nullable=False, default=0)


class PlayerBasketDBModel(Base, CreateUpdateDate):
    __tablename__ = 'player_baskets'

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"))
    player: Mapped["PlayerDBModel"] = relationship()
    basket: Mapped[int] = mapped_column(default=4)

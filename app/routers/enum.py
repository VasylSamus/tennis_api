from fastapi import APIRouter

from pydantic_models.enum import *


enum_router = APIRouter()


@enum_router.get("/")
async def root():
    return {
        "hand": to_dict(HandEnum),
        "backhand_type": to_dict(BackhandTypeEnum),
        "match_type": to_dict(MatchTypeEnum),
        "gender": to_dict(GenderEnum),
        "surface_type": to_dict(SurfaceTypeEnum),
        "tournament_stage_type": to_dict(TournamentStageTypeEnum),
    }


@enum_router.get("/hand")
async def get_hand_enum():
    return to_dict(HandEnum)


@enum_router.get("/backhand_type")
async def get_backhand_type_enum():
    return to_dict(BackhandTypeEnum)


@enum_router.get("/match_type")
async def get_match_type_enum():
    return to_dict(MatchTypeEnum)


@enum_router.get("/gender")
async def get_gender_enum():
    return to_dict(GenderEnum)


@enum_router.get("/surface_type")
async def get_surface_type_enum():
    return to_dict(SurfaceTypeEnum)


@enum_router.get("/tournament_stage_type")
async def get_tournament_stage_type_enum():
    return to_dict(TournamentStageTypeEnum)

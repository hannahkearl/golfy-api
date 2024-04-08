from uuid import UUID

from pydantic import BaseModel



class Player(BaseModel):
    id: UUID
    name = str
    handicap = float

class CreatePlayerRequest(BaseModel):
    name = str
    handicap = float

class ListPlayersResponse(BaseModel):
    id

class PlayerResponse(BaseModel):
    id: UUID   
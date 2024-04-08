import uuid

from fastapi import FastAPI

from models.course import Course
from models.player import Player, CreatePlayerRequest, PlayerResponse


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}

@app.get("/courses")
@app.post("/courses")
@app.put("/courses/{course_id}")
@app.delete("/courses/{course_id}")

@app.get("/players")
async def get_players() -> list[Player]:
    return players.values()

@app.post("/players")
async def create_players(player_detail: CreatePlayerRequest) -> PlayerResponse:
    player_id = uuid.uuid4()
    players[player_id] = Player
    return PlayerResponse(id=player_id)

@app.put("/players/{player_id}")
async def update_player(player_id: uuid.UUID, updated_player: Player) -> uuid.UUID:
    players[player_id] = updated_player    
    return player_id

@app.delete("/players/{player_id}")
async def del_player(player_id: uuid.UUID) -> None:
    players.pop(player_id)
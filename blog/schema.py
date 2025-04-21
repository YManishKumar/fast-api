from pydantic import BaseModel

# Used when creating a tournament (client input)
class TournamentCreateSchema(BaseModel):
    name: str
    description: str
    start_date: str
    end_date: str
    location: str
    max_teams: int
    prize_pool: float
    game_type: str
    contact_info: str
    registration_fee: float
    status: str

    class Config:
        orm_mode = True
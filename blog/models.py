from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Tournament(Base):
    __tablename__ = "tournaments"

    tournament_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    location = Column(String)
    max_teams = Column(Integer)
    prize_pool = Column(Float)
    game_type = Column(String)
    contact_info = Column(String)
    registration_fee = Column(Float)
    status = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    created_by = Column(String)
    updated_by = Column(String)

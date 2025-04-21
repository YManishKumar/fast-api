from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text 
from blog import database
from blog.models import Tournament
from datetime import datetime, timezone
from blog.schema import TournamentCreateSchema
from blog.database import engine, Base
from typing import List


app = FastAPI()

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))  # fixed with text()
        return {"status": "Connected ✅"}
    except Exception as e:
        return {"status": "Failed ❌", "error": str(e)}


@app.post('/createTournament',)
def createTournament(req: List[TournamentCreateSchema], db: Session = Depends(get_db)):
    tournaments = []

    for tournament_data in req:
        new_tournament = Tournament(
            name=tournament_data.name,
            description=tournament_data.description,
            start_date=tournament_data.start_date,
            end_date=tournament_data.end_date,
            location=tournament_data.location,
            max_teams=tournament_data.max_teams,
            prize_pool=tournament_data.prize_pool,
            game_type=tournament_data.game_type,
            contact_info=tournament_data.contact_info,
            registration_fee=tournament_data.registration_fee,
            status=tournament_data.status,
            created_by="system",
            updated_by="system",
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=datetime.now(timezone.utc).isoformat()
        )
        db.add(new_tournament)

        # you can choose to commit per item, or batch-commit later
        db.commit()
        db.refresh(new_tournament)

        tournaments.append({
            "message": "Tournament Created Successfully ✅",
            "tournament_id": new_tournament.tournament_id
        })

    # ← return after the loop finishes
    return {"tournaments": tournaments}


@app.get('/getTournaments')
def getTournaments(db: Session = Depends(get_db)):
    tournaments = db.query(Tournament).all()
    return {"tournaments": tournaments}

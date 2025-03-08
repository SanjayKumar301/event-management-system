from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Event, Attendee
from manager import EventManager, Scheduler
from database import Database
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
db = Database()
manager = EventManager(db)
scheduler = Scheduler(db)  # Pass the db instance here

class EventCreate(BaseModel):
    id: str
    title: str
    date: str
    capacity: int
    type: str = "basic"
    instructor: str | None = None

class AttendeeCreate(BaseModel):
    id: str
    name: str
    email: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Event Management System API"}

@app.post("/events")
def create_event(event: EventCreate):
    evt = Event(event.id, event.title, event.date, event.capacity, event.type, event.instructor)
    try:
        if manager.add_event(evt):
            scheduler.schedule_event(evt)
            return {"message": "Event created", "event": evt.display_details()}
        raise HTTPException(status_code=400, detail="Event ID already exists")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/events")
def list_events():
    events = manager.list_events()
    return [{"id": e.id, "title": e.title, "date": str(e.date), "attendees": 0} for e in events]  # Attendees count TBD

@app.post("/events/{event_id}/register")
def register_attendee(event_id: str, attendee: AttendeeCreate):
    event = manager.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    att = Attendee(attendee.id, attendee.name, attendee.email)
    if db.register_attendee(event_id, att.id):
        db.add_attendee(att)
        return {"message": f"{att.name} registered for {event.title}"}
    raise HTTPException(status_code=400, detail="Event is full or registration failed")

@app.get("/scheduler/next")
def get_next_event():
    next_event = scheduler.get_next_event()
    if next_event:
        date, event_id = next_event
        event = manager.get_event(event_id)
        return {"title": event.title, "date": str(date)}
    return {"message": "No scheduled events"}
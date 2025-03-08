import heapq
from datetime import datetime, timedelta
from models import Event
from database import Database

class EventManager:
    def __init__(self, db: Database):
        self.db = db
        self.events = {}

    def add_event(self, event: Event) -> bool:
        if self.db.add_event(event):
            self.events[event.id] = event
            return True
        return False

    def get_event(self, event_id: str) -> Event | None:
        if event_id in self.events:
            return self.events[event_id]
        event_data = self.db.get_event(event_id)
        if event_data:
            evt = Event(event_data["id"], event_data["title"], event_data["date"], event_data["capacity"], event_data["type"], event_data["instructor"])
            self.events[event_id] = evt
            return evt
        return None

    def list_events(self) -> list[Event]:
        db_events = self.db.list_events()
        events = []
        for e in db_events:
            evt = Event(e["id"], e["title"], e["date"], e["capacity"], e["type"], e["instructor"])
            self.events[e["id"]] = evt
            events.append(evt)
        return events

class Scheduler:
    def __init__(self, db: Database):
        self.db = db
        self.event_queue = []

    def schedule_event(self, event: Event):
        for existing_date, existing_id in self.event_queue:
            existing_event = self.db.get_event(existing_id)
            if existing_event:
                existing_start = datetime.strptime(existing_event["date"], "%Y-%m-%dT%H:%M:%S")
                existing_end = existing_start + timedelta(hours=1)
                new_start = event.date
                new_end = new_start + timedelta(hours=1)
                if new_start < existing_end and new_end > existing_start:
                    raise ValueError(f"Conflict with event {existing_event['title']} at {existing_event['date']}")
        heapq.heappush(self.event_queue, (event.date, event.id))

    def get_next_event(self) -> tuple[datetime, str] | None:
        return self.event_queue[0] if self.event_queue else None
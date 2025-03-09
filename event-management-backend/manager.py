import heapq
from datetime import datetime, timedelta
from models import Event
from database import Database
from intervaltree import IntervalTree

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

    def delete_event(self, event_id: str) -> bool:
        if self.db.delete_event(event_id):
            self.events.pop(event_id, None)
            return True
        return False

    def update_event(self, event_id: str, title=None, date=None, capacity=None, type=None, instructor=None) -> bool:
        if self.db.update_event(event_id, title, date, capacity, type, instructor):
            event_data = self.db.get_event(event_id)
            if event_data:
                evt = Event(event_data["id"], event_data["title"], event_data["date"], event_data["capacity"], event_data["type"], event_data["instructor"])
                self.events[event_id] = evt
            return True
        return False

class Scheduler:
    def __init__(self, db: Database):
        self.db = db
        self.event_queue = []
        self.intervals = IntervalTree()

    def schedule_event(self, event: Event):
        start = event.date
        end = start + timedelta(hours=1)  # Assume 1-hour events
        start_ts = start.timestamp()
        end_ts = end.timestamp()
        
        # Check for overlaps
        if self.intervals.overlaps(start_ts, end_ts):
            overlapping = self.intervals[start_ts:end_ts]
            conflicting_id = next(iter(overlapping)).data
            conflicting_event = self.db.get_event(conflicting_id)
            raise ValueError(f"Conflict with event {conflicting_event['title']} at {conflicting_event['date']}")
        
        # Add to interval tree and priority queue
        self.intervals[start_ts:end_ts] = event.id
        heapq.heappush(self.event_queue, (event.date, event.id))

    def get_next_event(self) -> tuple[datetime, str] | None:
        return self.event_queue[0] if self.event_queue else None
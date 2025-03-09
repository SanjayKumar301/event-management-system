# models.py
from datetime import datetime
import uuid

class Event:
    def __init__(self, id: str, title: str, date: str, capacity: int, type: str = "basic", instructor: str = None):
        self.id = id
        self.title = title
        # Try parsing ISO format first, then fallback to "YYYY-MM-DD HH:MM"
        try:
            self.date = datetime.fromisoformat(date)  # Handles "2025-03-10T14:00:00"
        except ValueError:
            self.date = datetime.strptime(date, "%Y-%m-%d %H:%M")  # Fallback for "2025-03-10 14:00"
        self.capacity = capacity
        self.type = type
        self.instructor = instructor

    def display_details(self) -> str:
        return f"Event: {self.title}, Date: {self.date}, Capacity: {self.capacity}"

class Attendee:
    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
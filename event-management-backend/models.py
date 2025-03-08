from datetime import datetime

class Event:
    def __init__(self, id: str, title: str, date: str, capacity: int, type: str = "basic", instructor: str = None):
        self._id = id
        self._title = title
        # Handle ISO format from database
        self._date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S") if 'T' in date else datetime.strptime(date, "%Y-%m-%d %H:%M")
        self._capacity = capacity
        self._type = type
        self._instructor = instructor

    @property
    def id(self): return self._id
    @property
    def title(self): return self._title
    @property
    def date(self): return self._date
    @property
    def capacity(self): return self._capacity
    @property
    def type(self): return self._type
    @property
    def instructor(self): return self._instructor

    def display_details(self) -> str:
        base = f"Event: {self._title}, Date: {self._date}, Capacity: {self._capacity}"
        return f"{base}, Instructor: {self._instructor}" if self._instructor else base

# Inherited class (example of inheritance)
class WorkshopEvent(Event):
    def __init__(self, id: str, title: str, date: str, capacity: int, instructor: str):
        super().__init__(id, title, date, capacity)
        self._instructor = instructor

    def display_details(self) -> str:  # Polymorphism
        return f"Workshop: {self._title}, Instructor: {self._instructor}, Date: {self._date}"

class Attendee:
    def __init__(self, id: str, name: str, email: str):
        self._id = id
        self._name = name
        self._email = email

    @property
    def id(self): return self._id
    @property
    def name(self): return self._name
    @property
    def email(self): return self._email
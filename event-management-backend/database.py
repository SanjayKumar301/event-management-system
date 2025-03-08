import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="events.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        # Events table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                date TEXT NOT NULL,
                capacity INTEGER NOT NULL,
                type TEXT NOT NULL,
                instructor TEXT
            )
        ''')
        # Attendees table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendees (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        # Event-Attendee relationship (many-to-many)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS event_attendees (
                event_id TEXT,
                attendee_id TEXT,
                FOREIGN KEY (event_id) REFERENCES events(id),
                FOREIGN KEY (attendee_id) REFERENCES attendees(id),
                PRIMARY KEY (event_id, attendee_id)
            )
        ''')
        self.conn.commit()

    def add_event(self, event):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO events (id, title, date, capacity, type, instructor)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (event.id, event.title, event.date.isoformat(), event.capacity, event.type, event.instructor))
        self.conn.commit()
        return cursor.rowcount > 0

    def get_event(self, event_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "title": row[1], "date": row[2], "capacity": row[3], "type": row[4], "instructor": row[5]}
        return None

    def list_events(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM events')
        rows = cursor.fetchall()
        return [{"id": r[0], "title": r[1], "date": r[2], "capacity": r[3], "type": r[4], "instructor": r[5]} for r in rows]

    def add_attendee(self, attendee):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO attendees (id, name, email)
            VALUES (?, ?, ?)
        ''', (attendee.id, attendee.name, attendee.email))
        self.conn.commit()

    def register_attendee(self, event_id, attendee_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM event_attendees WHERE event_id = ?', (event_id,))
        current_attendees = cursor.fetchone()[0]
        cursor.execute('SELECT capacity FROM events WHERE id = ?', (event_id,))
        capacity = cursor.fetchone()[0]
        
        if current_attendees < capacity:
            cursor.execute('''
                INSERT OR IGNORE INTO event_attendees (event_id, attendee_id)
                VALUES (?, ?)
            ''', (event_id, attendee_id))
            self.conn.commit()
            return cursor.rowcount > 0
        return False

    def close(self):
        self.conn.close()
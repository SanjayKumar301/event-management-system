# Event Management System\n\nA system for managing events with a Python FastAPI backend and Next.js frontend.\n\n- **Backend**: Located in , uses FastAPI and SQLite.\n- **Frontend**: Located in , will use Next.js (TBD).



##### 1. GET / (Root Endpoint)


```
curl -X GET "http://127.0.0.1:8000/"
```

##### 2. POST /events (Create Event)

   - Test 1: Successful Event Creation
	   

```
curl -X POST "http://127.0.0.1:8000/events" -H "Content-Type: application/json" -d '{"id": "e1", "title": "DSA Workshop", "date": "2025-03-10 14:00", "capacity": 10}'
```

- Test 2: Duplicate Event ID

```
curl -X POST "http://127.0.0.1:8000/events" -H "Content-Type: application/json" -d '{"id": "e1", "title": "Another DSA", "date": "2025-03-11 15:00", "capacity": 15}'
```


##### 3. GET /events (List Events)
             
   - Test 1: List Empty Events

```
curl -X GET "http://127.0.0.1:8000/events"
```

   - Test 2: List Populated Events


```
curl -X GET "http://127.0.0.1:8000/events"
```


##### 4. POST /events/{event_id}/register (Register Attendee)

   - Test 1: Successful Registration

```
curl -X POST "http://127.0.0.1:8000/events/e1/register" -H "Content-Type: application/json" -d '{"id": "a1", "name": "Alice", "email": "alice@example.com"}'
```

   -Test 2: Event Not Found
	
```
curl -X POST "http://127.0.0.1:8000/events/e99/register" -H "Content-Type: application/json" -d '{"id": "a2", "name": "Bob", "email": "bob@example.com"}'
```

   - Test 3: Capacity Full

```
curl -X POST "http://127.0.0.1:8000/events/e1/register" -H "Content-Type: application/json" -d '{"id": "a11", "name": "Charlie", "email": "charlie@example.com"}'
```

   - Test 4: Duplicate Attendee ID

```
curl -X POST "http://127.0.0.1:8000/events/e1/register" -H "Content-Type: application/json" -d '{"id": "a1", "name": "Alice2", "email": "alice2@example.com"}'
```


##### 5. DELETE /events/{event_id} (Delete Event)

   - Test 1: Successful Deletion

```
curl -X DELETE "http://127.0.0.1:8000/events/e1"
```

   - Test 2: Event Not Found

```
curl -X DELETE "http://127.0.0.1:8000/events/e99"
```


##### 6. PUT /events/{event_id} (Update Event)

   - Test 1: Successful Update

```
curl -X PUT "http://127.0.0.1:8000/events/e1" -H "Content-Type: application/json" -d '{"title": "Updated DSA"}'
```

   - Test 2: Event Not Found

```
curl -X PUT "http://127.0.0.1:8000/events/e99" -H "Content-Type: application/json" -d '{"title": "Nonexistent"}'
```

   - Invalid Date Update

```
curl -X PUT "http://127.0.0.1:8000/events/e1" -H "Content-Type: application/json" -d '{"date": "2025-13-01 14:00"}'
```

##### 7. GET /scheduler/next (Next Event)

   - Test 1: Next Event Exists

```
curl -X GET "http://127.0.0.1:8000/scheduler/next"
```

   - Test 2: No Events

```
curl -X GET "http://127.0.0.1:8000/scheduler/next"
```

import Link from 'next/link';

type Event = {
  id: string;
  title: string;
  date: string;
  attendees: number;
};

export default function EventList({ events }: { events: Event[] }) {
  return (
    <div className="mt-4">
      <h2 className="text-xl font-semibold">Events</h2>
      <ul className="mt-2 space-y-2">
        {events.map((event) => (
          <li key={event.id} className="border p-2 rounded">
            <Link href={`/events/${event.id}`} className="text-blue-600">
              {event.title}
            </Link>
            <p>Date: {new Date(event.date).toLocaleString()}</p>
            <p>Attendees: {event.attendees}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

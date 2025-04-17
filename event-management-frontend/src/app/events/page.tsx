import EventList from '../../components/EventList';
import { getEvents } from '../../lib/api';
import Link from 'next/link';

export default async function Events() {
  const events = await getEvents();

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Events</h1>
      <Link href="/events/create" className="text-blue-600 mt-4 block">
        Create New Event
      </Link>
      <EventList events={events} />
    </div>
  );
}

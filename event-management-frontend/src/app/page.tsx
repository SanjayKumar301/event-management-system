import { getNextEvent } from '../lib/api';

export default async function Home() {
  const nextEvent = await getNextEvent();

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Event Management System</h1>
      <div className="mt-4">
        <h2 className="text-xl font-semibold">Next Event</h2>
        {nextEvent.title ? (
          <p>
            {nextEvent.title} on {new Date(nextEvent.date).toLocaleString()}
          </p>
        ) : (
          <p>No upcoming events</p>
        )}
      </div>
      <a href="/events" className="text-blue-600 mt-4 block">
        View All Events
      </a>
    </div>
  );
}

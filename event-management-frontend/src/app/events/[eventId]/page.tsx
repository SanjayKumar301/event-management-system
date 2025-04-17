import RegisterForm from '../../../components/RegisterForm';
import { getEvents } from '../../../lib/api';

export default async function EventDetail({ params }: { params: { eventId: string } }) {
  const events = await getEvents();
  const event = events.find((e: any) => e.id === params.eventId);

  if (!event) {
    return <div className="container mx-auto p-4">Event not found</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">{event.title}</h1>
      <p>Date: {new Date(event.date).toLocaleString()}</p>
      <p>Attendees: {event.attendees}</p>
      <RegisterForm eventId={params.eventId} />
    </div>
  );
}

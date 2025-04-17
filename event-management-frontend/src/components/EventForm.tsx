'use client'; // Client-side component

import { useState } from 'react';
import { createEvent } from '../lib/api';

export default function EventForm() {
  const [form, setForm] = useState({ id: '', title: '', date: '', capacity: '', type: 'basic', instructor: '' });
  const [message, setMessage] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await createEvent({
        id: form.id,
        title: form.title,
        date: form.date,
        capacity: parseInt(form.capacity),
        type: form.type,
        instructor: form.instructor || undefined,
      });
      setMessage('Event created!');
      setForm({ id: '', title: '', date: '', capacity: '', type: 'basic', instructor: '' });
    } catch (error) {
      setMessage('Error creating event');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mt-4 space-y-4">
      <div>
        <label className="block">ID</label>
        <input
          type="text"
          value={form.id}
          onChange={(e) => setForm({ ...form, id: e.target.value })}
          className="border p-2 w-full"
          required
        />
      </div>
      <div>
        <label className="block">Title</label>
        <input
          type="text"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
          className="border p-2 w-full"
          required
        />
      </div>
      <div>
        <label className="block">Date (YYYY-MM-DD HH:MM)</label>
        <input
          type="text"
          value={form.date}
          onChange={(e) => setForm({ ...form, date: e.target.value })}
          className="border p-2 w-full"
          required
        />
      </div>
      <div>
        <label className="block">Capacity</label>
        <input
          type="number"
          value={form.capacity}
          onChange={(e) => setForm({ ...form, capacity: e.target.value })}
          className="border p-2 w-full"
          required
        />
      </div>
      <div>
        <label className="block">Type</label>
        <select
          value={form.type}
          onChange={(e) => setForm({ ...form, type: e.target.value })}
          className="border p-2 w-full"
        >
          <option value="basic">Basic</option>
          <option value="workshop">Workshop</option>
        </select>
      </div>
      <div>
        <label className="block">Instructor</label>
        <input
          type="text"
          value={form.instructor}
          onChange={(e) => setForm({ ...form, instructor: e.target.value })}
          className="border p-2 w-full"
        />
      </div>
      <button type="submit" className="bg-blue-500 text-white p-2 rounded">
        Create Event
      </button>
      {message && <p className="mt-2">{message}</p>}
    </form>
  );
}

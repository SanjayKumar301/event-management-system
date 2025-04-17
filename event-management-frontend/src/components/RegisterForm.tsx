'use client';

import { useState } from 'react';
import { registerAttendee } from '../lib/api';

export default function RegisterForm({ eventId }: { eventId: string }) {
  const [form, setForm] = useState({ id: '', name: '', email: '' });
  const [message, setMessage] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await registerAttendee(eventId, form);
      setMessage('Registered successfully!');
      setForm({ id: '', name: '', email: '' });
    } catch (error) {
      setMessage('Error registering');
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
        <label className="block">Name</label>
        <input
          type="text"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
          className="border p-2 w-full"
          required
        />
      </div>
      <div>
        <label className="block">Email</label>
        <input
          type="email"
          value={form.email}
          onChange={(e) => setForm({ ...form, email: e.target.value })}
          className="border p-2 w-full"
          required
        />
      </div>
      <button type="submit" className="bg-blue-500 text-white p-2 rounded">
        Register
      </button>
      {message && <p className="mt-2">{message}</p>}
    </form>
  );
}

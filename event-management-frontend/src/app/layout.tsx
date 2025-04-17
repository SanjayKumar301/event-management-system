import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Event Management System',
  description: 'Manage events with ease',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-gray-100">
        <nav className="bg-blue-500 text-white p-4">
          <a href="/" className="mr-4">Home</a>
          <a href="/events">Events</a>
        </nav>
        {children}
      </body>
    </html>
  );
}

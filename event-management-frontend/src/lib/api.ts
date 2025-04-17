import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'; // Backend URL

export const getEvents = async () => {
  const response = await axios.get(`${API_URL}/events`);
  return response.data;
};

export const createEvent = async (event: {
  id: string;
  title: string;
  date: string;
  capacity: number;
  type?: string;
  instructor?: string;
}) => {
  const response = await axios.post(`${API_URL}/events`, event);
  return response.data;
};

export const registerAttendee = async (eventId: string, attendee: {
  id: string;
  name: string;
  email: string;
}) => {
  const response = await axios.post(`${API_URL}/events/${eventId}/register`, attendee);
  return response.data;
};

export const getNextEvent = async () => {
  const response = await axios.get(`${API_URL}/scheduler/next`);
  return response.data;
};

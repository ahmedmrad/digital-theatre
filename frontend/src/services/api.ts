// src/services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
});

export const getPlays = async () => {
  const response = await api.get('/plays');
  return response.data;
};

export const getPlay = async (id: string) => {
  const response = await api.get(`/plays/${id}`);
  return response.data;
};

export const createPlay = async (playData: any) => {
  const response = await api.post('/plays', playData);
  return response.data;
};
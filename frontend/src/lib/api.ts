import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  withCredentials: true,
});

export const auth = {
  startGoogleOAuth: async () => {
    const { data } = await api.get('/auth/google/start');
    return data;
  },
  callback: async (code: string) => {
    const { data } = await api.post('/auth/google/callback', { code });
    return data;
  }
};

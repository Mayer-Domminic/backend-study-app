import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const loginUser = async (email: string, password: string) => {
  try {
    const response = await api.post('/users/login', { email, password });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const registerUser = async (username: string, email: string, password: string) => {
  try {
    const response = await api.post('/users/', { username, email, password });
    return response.data;
  } catch (error) {
    throw error;
  }
};
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interfaces
export interface LoginResponse {
  access_token: string;
  token_type: string;
  user_id: number;
}

export interface UserResponse {
  user_id: number;
  username: string;
  email: string;
}

export interface RegisterResponse {
  user: UserResponse;
  access_token: string;
  token_type: string;
  user_id: number;
}

// Login User
export const loginUser = async (email: string, password: string): Promise<LoginResponse> => {
  const formData = new URLSearchParams();
  formData.append('username', email); // user === email...
  formData.append('password', password);

  const response = await api.post<LoginResponse>('/users/login', formData, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });
  return response.data;
};

// Register User
export const registerUser = async (
  username: string,
  email: string,
  password: string
): Promise<RegisterResponse> => {
  const response = await api.post<RegisterResponse>('/users/register', {
    username,
    email,
    password,
  });
  return response.data;
};

export const setAuthToken = (token: string) => {
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
};

export const logoutUser = async () => {
  // Remove token and user ID from cookies
  //Cookies.remove('userToken');
  //Cookies.remove('userId');
  // Optionally, reset the authorization header
  delete api.defaults.headers.common['Authorization'];
};

export interface Item {
  id: number;               // Corresponds to item_id
  user_id: number;         // Corresponds to user_id
  tag_id: number;          // Corresponds to tag_id
  name: string;            // Corresponds to name
  difficulty: string | null; // Corresponds to difficulty (nullable)
  number: number | null;   // Corresponds to number (nullable)
  src: string | null;      // Corresponds to src (nullable)
  created_at: string;      // Corresponds to created_at
}


export const getUserItems = async (userId: number): Promise<Item[]> => {
  try {
    const response = await api.get(`/items/user/${userId}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};


export interface UserSettings {
  setting_id: number;
  user_id: number;
  grind: number;
  problems_per_day: number;
  noti_time: number;
  days_of_week: string;
}

export const getUserSettings = async (userId: number): Promise<UserSettings> => {
  const response = await api.get(`/settings/${userId}`);
  return response.data;
};

export const updateUserSettings = async (userId: number, settings: Partial<UserSettings>): Promise<UserSettings> => {
  const response = await api.put(`/settings/${userId}`, settings);
  return response.data;
};



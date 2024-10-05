import React from 'react';
import { logoutUser } from '@/lib/api';
import { useNavigate } from 'react-router-dom';

const LogoutButton = () => {
  const navigate = useNavigate();
  const handleLogout = async () => {
    try {
      await logoutUser();
      navigate('/');
    } catch (error) {
      console.error('Logout failed', error);
    }
  };

  return (
    <div className="space-y-2">
        <button onClick={handleLogout} className="btn btn-danger">Logout</button>
    </div>
  );
};

export default LogoutButton;

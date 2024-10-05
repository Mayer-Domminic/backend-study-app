import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Cookies from 'js-cookie';
import { getUserItems, getUserSettings, Item, UserSettings } from '@/lib/api';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { AlertCircle } from 'lucide-react';
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";

const Home = () => {
  const navigate = useNavigate();
  const [items, setItems] = useState<Item[]>([]);
  const [settings, setSettings] = useState<UserSettings | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUserData = async () => {
      const userToken = Cookies.get('userToken');
      const userId = Number(Cookies.get('user_id'));

      if (!userToken || !userId) {
        console.log(userToken)
        console.log(userId)
        console.log(Cookies.get('userId'))
        navigate('/');
        return;
      }

      try {
        setLoading(true);
        const [userItems, userSettings] = await Promise.all([
          getUserItems(Number(userId)),
          getUserSettings(Number(userId))
        ]);
        
        setItems(userItems);
        setSettings(userSettings);
        setError(null);
      } catch (err) {
        setError('Failed to load user data. Please try again later.');
        console.error('Error fetching user data:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchUserData();
  }, [navigate]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-gray-900"></div>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Welcome to Your Dashboard</h1>
      
      {error && (
        <Alert variant="destructive">
          <AlertCircle className="h-4 w-4" />
          <AlertTitle>Error</AlertTitle>
          <AlertDescription>{error}</AlertDescription>
        </Alert>
      )}

      {settings && (
        <Card className="mb-6">
          <CardHeader>
            <CardTitle>Your Practice Settings</CardTitle>
            <CardDescription>Current study configuration</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <p className="font-semibold">Difficulty Level:</p>
                <p>{settings.grind}</p>
              </div>
              <div>
                <p className="font-semibold">Problems Per Day:</p>
                <p>{settings.problems_per_day}</p>
              </div>
              <div>
                <p className="font-semibold">Notification Time:</p>
                <p>{settings.noti_time}:00</p>
              </div>
              <div>
                <p className="font-semibold">Practice Days:</p>
                <p>{settings.days_of_week.split(',').join(', ')}</p>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {items.map((item) => (
          <Card key={item.id}>
            <CardHeader>
              <CardTitle>{item.name}</CardTitle>
            </CardHeader>
            <CardContent>
              <p>{item.difficulty}</p>
              <p>{item.created_at}</p>
              {/* Add any additional properties you want to display */}
            </CardContent>
          </Card>
        ))}
      </div>

      {items.length === 0 && (
        <Card>
          <CardContent className="p-6">
            <p className="text-center text-gray-500">No items found. Start adding some!</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default Home;

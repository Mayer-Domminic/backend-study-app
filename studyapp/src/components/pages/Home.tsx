import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Cookies from 'js-cookie';
import { getUserItems, Item } from '@/lib/api';
import { LoadingSkeleton } from '@/components/LoadingSkeleton';
import { ErrorAlert } from '@/components/ErrorAlert';
import { ItemCard } from '@/components/ItemCard';
import { EmptyState } from '@/components/EmptyState';
import { CreateItemButton } from '@/components/CreateItemButton';

export function Home() {
  const navigate = useNavigate();
  const [items, setItems] = useState<Item[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUserData = async () => {
      const userToken = Cookies.get('userToken');
      const userId = Number(Cookies.get('userId'));

      if (!userToken || !userId) {
        navigate('/');
        return;
      }

      try {
        setLoading(true);
        const userItems = await getUserItems(userId);
        setItems(userItems);
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
    return <LoadingSkeleton />;
  }


  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Welcome to Your Dashboard</h1>
      
      {error && <ErrorAlert message={error} />}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {items.map((item) => (
          <ItemCard key={item.id} item={item} />
        ))}
        <CreateItemButton />
      </div>

      {items.length === 0 && <EmptyState />}
    </div>
  );
}

export default Home;
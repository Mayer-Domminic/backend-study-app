import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { getUserSettings, updateUserSettings, UserSettings } from '@/lib/api';
import Cookies from 'js-cookie';

export default function SettingsPage() {
  const navigate = useNavigate();
  const [settings, setSettings] = useState<UserSettings | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');
  const userId = parseInt(Cookies.get('userId') || '0');

  useEffect(() => {
    const fetchSettings = async () => {
      try {
        const userSettings = await getUserSettings(userId);
        setSettings(userSettings);
      } catch (err) {
        setError('Failed to load settings');
      } finally {
        setIsLoading(false);
      }
    };

    fetchSettings();
  }, [userId]);

  const handleSave = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!settings) return;

    try {
      const updatedSettings = await updateUserSettings(userId, settings);
      setSettings(updatedSettings);
      // Show success message or toast
    } catch (err) {
      setError('Failed to update settings');
    }
  };

  if (isLoading) return <div>Loading settings...</div>;
  if (error) return <div className="text-red-500">{error}</div>;
  if (!settings) return <div>No settings found</div>;

  return (
    <div className="container mx-auto p-4">
      <Card>
        <CardHeader>
          <CardTitle>User Settings</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSave} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="grind">Grind Level</Label>
              <Select 
                value={settings.grind.toString()} 
                onValueChange={(value) => setSettings({...settings, grind: parseInt(value)})}
              >
                <SelectTrigger>
                  <SelectValue placeholder="Select grind level" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="1">Easy</SelectItem>
                  <SelectItem value="2">Medium</SelectItem>
                  <SelectItem value="3">Hard</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="problems_per_day">Problems Per Day</Label>
              <Input
                id="problems_per_day"
                type="number"
                value={settings.problems_per_day}
                onChange={(e) => setSettings({...settings, problems_per_day: parseInt(e.target.value)})}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="noti_time">Notification Time</Label>
              <Input
                id="noti_time"
                type="number"
                min="0"
                max="23"
                value={settings.noti_time}
                onChange={(e) => setSettings({...settings, noti_time: parseInt(e.target.value)})}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="days_of_week">Days of Week</Label>
              <Input
                id="days_of_week"
                value={settings.days_of_week}
                onChange={(e) => setSettings({...settings, days_of_week: e.target.value})}
                placeholder="e.g., 1,2,3,4,5"
              />
            </div>

            <div className="flex justify-between">
              <Button type="submit">Save Settings</Button>
              <Button type="button" variant="outline" onClick={() => navigate('/home')}>
                Back to Home
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
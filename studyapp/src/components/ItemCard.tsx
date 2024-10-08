import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Item } from '@/lib/api';
import { CreateAttemptButton } from './CreateAttemptButton';

interface ItemCardProps {
  item: Item;
}

export function ItemCard({ item }: ItemCardProps) {
  return (
    <Card key={item.id}>
      <CardHeader>
        <CardTitle>{item.name}</CardTitle>
      </CardHeader>
      <CardContent>
        <p>{item.difficulty}</p>
        <p>{item.created_at}</p>
        <CreateAttemptButton item={item} />
      </CardContent>
    </Card>
  );
}
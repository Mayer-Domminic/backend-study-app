import { Card, CardContent } from "@/components/ui/card";

export function EmptyState() {
  return (
    <Card>
      <CardContent className="p-6">
        <p className="text-center text-gray-500">No items found. Start adding some!</p>
      </CardContent>
    </Card>
  );
}
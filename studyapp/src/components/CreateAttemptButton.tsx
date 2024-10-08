import { Plus } from 'lucide-react';
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { CreateAttemptForm } from './CreateAttemptForm';
import { Item } from '@/lib/api';

interface CreateAttemptButtonProps {
  item: Item;
}

export function CreateAttemptButton({ item }: CreateAttemptButtonProps) {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="secondary" size="sm">
          <Plus className="mr-2 h-4 w-4" /> Add Attempt
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Add Attempt for {item.name}</DialogTitle>
        </DialogHeader>
        <CreateAttemptForm itemId={item.id} />
      </DialogContent>
    </Dialog>
  );
}
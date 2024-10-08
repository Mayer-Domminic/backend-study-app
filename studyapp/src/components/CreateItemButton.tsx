import { Plus } from 'lucide-react';
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { CreateItemForm } from './CreateItemForm';

export function CreateItemButton() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline" className="h-[200px] w-full">
          <Plus className="mr-2 h-4 w-4" /> Add New Item
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Create New Item</DialogTitle>
        </DialogHeader>
        <CreateItemForm />
      </DialogContent>
    </Dialog>
  );
}
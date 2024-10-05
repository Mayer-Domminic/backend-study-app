import React from 'react';
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { RegisterForm } from './register-form';
import { useNavigate } from 'react-router-dom';
import { UserPlus } from 'lucide-react';

export function RegisterButton() {
  const [isOpen, setIsOpen] = React.useState(false);
  const navigate = useNavigate();

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="w-full" variant="outline">
          <UserPlus className="mr-2 h-4 w-4" />
          Register
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Create Account</DialogTitle>
          <DialogDescription>
            Sign up for a new account to get started
          </DialogDescription>
        </DialogHeader>
        <RegisterForm onSuccess={() => {setIsOpen(false);navigate('/home');}} />
      </DialogContent>
    </Dialog>
  );
}
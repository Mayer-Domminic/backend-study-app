import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { LoginButton } from './auth/login-button';
import { RegisterButton } from './auth/register-button';

export function LandingCard() {
  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle className="text-3xl font-bold text-center">ProblemSolver</CardTitle>
        <CardDescription className="text-center text-lg">
          Track and improve your problem-solving skills
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="flex flex-col space-y-4 sm:flex-row sm:space-x-4 sm:space-y-0">
          <div className="flex-1">
            <LoginButton />
          </div>
          <div className="flex-1">
            <RegisterButton />
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
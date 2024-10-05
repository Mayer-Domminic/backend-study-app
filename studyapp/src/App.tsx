import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from "@/components/pages/Home";
import LandingPage from "@/components/pages/LandingPage";
import SettingsPage from "@/components/pages/Settings";
import LogoutPage from "@/components/pages/Logout";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/home" element={<Home />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path="/logout" element={<LogoutPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
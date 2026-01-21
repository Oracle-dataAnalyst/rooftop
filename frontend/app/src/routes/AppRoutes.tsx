import { Route, Routes } from "react-router-dom";

import Chat from "../pages/Chat";
import Home from "../pages/Home";
import Result from "../pages/Result";
import Simulation from "../pages/Simulation";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/simulation" element={<Simulation />} />
      <Route path="/result" element={<Result />} />
      <Route path="/chat" element={<Chat />} />
    </Routes>
  );
};

export default AppRoutes;

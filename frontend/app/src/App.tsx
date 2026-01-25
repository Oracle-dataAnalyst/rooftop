import { Link } from "react-router-dom";

import AppRoutes from "./routes/AppRoutes";

const App = () => {
  return (
    <main style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <header style={{ marginBottom: "2rem" }}>
        <h1>옥상이몽</h1>
        <nav style={{ display: "flex", gap: "1rem" }}>
          <Link to="/">홈</Link>
          <Link to="/simulation">시뮬레이션</Link>
          <Link to="/result">결과</Link>
          <Link to="/chat">챗봇</Link>
        </nav>
      </header>
      <AppRoutes />
    </main>
  );
};

export default App;

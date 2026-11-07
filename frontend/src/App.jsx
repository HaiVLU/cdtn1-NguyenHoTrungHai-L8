import React, { createContext, useContext, useState } from "react";
import { Navigate, Route, Routes, useNavigate } from "react-router-dom";
import Layout from "./components/Layout.jsx";
import OverviewPage from "./pages/OverviewPage.jsx";
import TechnicianReportPage from "./pages/TechnicianReportPage.jsx";
import SurveyDetailPage from "./pages/SurveyDetailPage.jsx";

const AuthContext = createContext(null);
export const useAuth = () => useContext(AuthContext);

function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();
    if (login(email.trim(), password)) {
      navigate("/admin", { replace: true });
    } else {
      setError("Email hoặc mật khẩu không chính xác.");
    }
  };

  return (
    <main className="auth-page">
      <form className="auth-card" onSubmit={handleSubmit}>
        <div className="auth-logo"><span>SC</span></div>
        <p className="auth-eyebrow">SMART CRM · ADMINISTRATION</p>
        <h1>Đăng nhập quản trị</h1>
        <p className="auth-description">Đăng nhập để truy cập hệ thống báo cáo CSAT/NPS.</p>
        <label className="auth-field">
          Email
          <input type="email" value={email} onChange={e => setEmail(e.target.value)}
            placeholder="Nhập email quản trị" autoComplete="username" required />
        </label>
        <label className="auth-field">
          Mật khẩu
          <input type="password" value={password} onChange={e => setPassword(e.target.value)}
            placeholder="Nhập mật khẩu" autoComplete="current-password" required />
        </label>
        {error && <div className="auth-error" role="alert">{error}</div>}
        <button className="auth-submit" type="submit">ĐĂNG NHẬP <span>→</span></button>
        <p className="auth-footnote">© Smart CRM · Hệ thống quản lý khảo sát</p>
      </form>
    </main>
  );
}

function AdminDashboard() {
  const navigate = useNavigate();
  const items = [
    { title: "Báo cáo tổng quan", description: "Theo dõi chỉ số CSAT, NPS và biểu đồ khảo sát.", path: "/", icon: "chart-line", number: "01" },
    { title: "Báo cáo kỹ thuật viên", description: "Xem kết quả khảo sát theo từng kỹ thuật viên.", path: "/technicians", icon: "users", number: "02" },
    { title: "Chi tiết phiếu khảo sát", description: "Xem nội dung và kết quả của một phiếu khảo sát.", path: "/surveys/1", icon: "file-text", number: "03" },
  ];
  const { logout } = useAuth();

  return (
    <main className="admin-page">
      <header className="admin-topbar">
        <div className="admin-brand"><span>SC</span><div><b>SMART CRM</b><small>ADMIN PORTAL</small></div></div>
        <button className="admin-logout" onClick={logout}>Đăng xuất <span>↗</span></button>
      </header>
      <section className="admin-welcome">
        <p className="auth-eyebrow">KHU VỰC QUẢN TRỊ</p>
        <h1>Xin chào, Admin <span>👋</span></h1>
        <p>Chọn một chức năng bên dưới để bắt đầu làm việc.</p>
      </section>
      <section className="admin-section">
        <div className="admin-section-heading"><div><h2>Không gian làm việc</h2><p>3 chức năng hiện có trong hệ thống</p></div><span>03 MODULES</span></div>
        <div className="admin-grid">
          {items.map(item => (
            <button className="admin-module" key={item.path} onClick={() => navigate(item.path)}>
              <div className="module-top"><span className="module-icon">{item.icon === "chart-line" ? "▥" : item.icon === "users" ? "♙" : "▤"}</span><span className="module-number">{item.number}</span></div>
              <h3>{item.title}</h3><p>{item.description}</p>
              <div className="module-open">MỞ CHỨC NĂNG <span>→</span></div>
            </button>
          ))}
        </div>
      </section>
      <footer className="admin-footer">SMART CRM · L8 CSAT/NPS <span>ADMINISTRATOR</span></footer>
    </main>
  );
}

function ProtectedLayout({ children }) {
  const { logout } = useAuth();
  return <Layout onLogout={logout}>{children}</Layout>;
}

export default function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(() => localStorage.getItem("smartcrm_admin_logged_in") === "true");
  const login = (email, password) => {
    if (email.toLowerCase() === "admin@gmail.com" && password === "123123") {
      localStorage.setItem("smartcrm_admin_logged_in", "true");
      setIsLoggedIn(true);
      return true;
    }
    return false;
  };
  const logout = () => {
    localStorage.removeItem("smartcrm_admin_logged_in");
    setIsLoggedIn(false);
  };

  return (
    <AuthContext.Provider value={{ login, logout }}>
      <Routes>
        <Route path="/login" element={isLoggedIn ? <Navigate to="/admin" replace /> : <LoginPage />} />
        <Route path="/admin" element={isLoggedIn ? <AdminDashboard /> : <Navigate to="/login" replace />} />
        <Route path="/*" element={isLoggedIn ? (
          <ProtectedLayout>
            <Routes>
              <Route path="/" element={<OverviewPage />} />
              <Route path="/technicians" element={<TechnicianReportPage />} />
              <Route path="/surveys/:id" element={<SurveyDetailPage />} />
              <Route path="*" element={<Navigate to="/admin" replace />} />
            </Routes>
          </ProtectedLayout>
        ) : <Navigate to="/login" replace />} />
      </Routes>
    </AuthContext.Provider>
  );
}

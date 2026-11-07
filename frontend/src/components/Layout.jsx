import React from "react";
import { NavLink } from "react-router-dom";

export default function Layout({ children, onLogout }) {
  return (
    <main className="window">
      <header className="titlebar">
        <span>SMART CRM — BÁO CÁO CSAT/NPS</span>
        <div className="layout-account">
          <span>ADMIN</span>
          <button type="button" onClick={onLogout}>ĐĂNG XUẤT</button>
        </div>
      </header>
      <nav className="nav">
        <NavLink to="/" end>Báo cáo tổng quan</NavLink>
        <NavLink to="/technicians">Kỹ thuật viên</NavLink>
        <NavLink to="/surveys/1">Chi tiết phiếu</NavLink>
        <NavLink to="/admin">Trang quản trị</NavLink>
      </nav>
      {children}
      <footer>Smart CRM · L8 CSAT/NPS</footer>
    </main>
  );
}


import React from "react";
import { NavLink } from "react-router-dom";

export default function Layout({ children }) {
  return (
    <main className="window">
      <header className="titlebar">
        <span>SMART CRM — BÁO CÁO CSAT/NPS</span>
        <span className="window-dots">
          <i />
          <i />
          <i />
        </span>
      </header>

      <nav className="nav">
        <NavLink to="/" end>
          Báo cáo tổng quan
        </NavLink>
        <NavLink to="/technicians">
          Kỹ thuật viên
        </NavLink>
        <NavLink to="/surveys/1">
          Chi tiết phiếu
        </NavLink>
      </nav>

      {children}

      <footer>Smart CRM · L8 CSAT/NPS</footer>
    </main>
  );
}

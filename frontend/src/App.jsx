
import React from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/Layout.jsx";
import OverviewPage from "./pages/OverviewPage.jsx";
import TechnicianReportPage from "./pages/TechnicianReportPage.jsx";
import SurveyDetailPage from "./pages/SurveyDetailPage.jsx";

export default function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<OverviewPage />} />
        <Route
          path="/technicians"
          element={<TechnicianReportPage />}
        />
        <Route
          path="/surveys/:id"
          element={<SurveyDetailPage />}
        />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Layout>
  );
}

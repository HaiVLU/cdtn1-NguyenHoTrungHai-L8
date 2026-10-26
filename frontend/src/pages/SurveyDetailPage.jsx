import React from "react";
import { useCallback, useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import DataState from "../components/DataState.jsx";
import { getSurvey } from "../api/reportApi.js";

export default function SurveyDetailPage(){
  const { id } = useParams();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const load = useCallback(async () => {
    setLoading(true); 
    setError('');
    try {
      setData(await getSurvey(id));
    } catch (e) { 
      setError(e.message); 
      setData(null); 
    } finally { 
      setLoading(false); 
    }
  }, [id]);

  useEffect(() => { 
    load(); 
  }, [load]);

  // Xử lý các trạng thái tải, lỗi và không có dữ liệu trước khi truy cập thuộc tính của dữ liệu
  if (loading) {
    return <section className="page">Đang tải thông tin khảo sát...</section>;
  }

  if (error) {
    return <section className="page">Lỗi: {error}</section>;
  }

  if (!data) {
    return <section className="page">Không tìm thấy khảo sát.</section>;
  }

  const phone = data?.phone; 
  const masked = phone ? String(phone).replace(/.(?=.{3})/g, '*') : '—';

  return (
    <section className="page detail-page">
      <h2>CHI TIẾT PHIẾU KHẢO SÁT</h2>
      <DataState loading={loading} error={error} isEmpty={!data} onRetry={load}>
        <div className="detail-group">
          <h3>Thông tin phiếu</h3>
          <div className="two-col">
            <ReadOnly label="Mã phiếu" value={data.response_id} />
            <ReadOnly label="Mã ticket" value={data.ticket_id} />
          </div>
          <ReadOnly label="Ngày khảo sát" value={data.responded_at ? new Date(data.responded_at).toLocaleDateString('vi-VN') : '—'} />
        </div>
        <div className="detail-group">
          <h3>Thông tin khách hàng và xử lí</h3>
          <ReadOnly label="Số điện thoại" value={masked} />
          <ReadOnly label="Trung tâm" value="— (API hiện tại chưa trả thông tin trung tâm)" />
          <ReadOnly label="Kỹ thuật viên" value="— (API hiện tại chưa trả thông tin kỹ thuật viên)" />
        </div>
        <h3>Kết quả khảo sát</h3>
        <div className="kpis">
          <Metric title="CSAT" value={data.score ?? '—'} note="Điểm nguồn 1–5" />
          <Metric title="NPS" value={data.nps_score ?? '—'} note="Điểm nguồn 0–10; không phải NPS tổng hợp" />
          <Metric title="SỐ PHIẾU" value="1" note="Chi tiết một phiếu" />
        </div>
        <div className="detail-group">
          <h3>Ý kiến khách hàng</h3>
          <p>{data.comment || 'Không có nội dung phản hồi.'}</p>
        </div>
      </DataState>
      <Link className="button-link" to="/technicians">QUAY LẠI</Link>
      <p className="hint">Backend hiện tại chỉ trả response_id, ticket_id, date_id, score, nps_score, comment và responded_at. Muốn hiện đúng trung tâm, kỹ thuật viên, điện thoại đã che và mã phiếu theo wireframe, cần mở rộng API chi tiết trả các trường liên quan từ PostgreSQL.</p>
    </section>
  );
}

function ReadOnly({ label, value }) {
  return (
    <label className="readonly">
      {label}
      <input readOnly value={value ?? '—'} />
    </label>
  );
}

function Metric({ title, value, note }) {
  return (
    <div className="metric">
      <strong>{title}</strong>
      <b>{value}</b>
      <small>{note}</small>
    </div>
  );
}
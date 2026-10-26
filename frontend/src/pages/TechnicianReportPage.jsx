import React from "react";
import { useCallback, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import DataState from "../components/DataState.jsx";
import { getTechnicians } from "../api/reportApi.js";

const DEMO = [
  { technicianId: 'DEMO-001', technicianName: 'Kỹ thuật viên demo A', surveyCount: 2, csat: { averageScore: 4.5 }, nps: { score: null, status: 'demo-unavailable' }, isDemo: true },
  { technicianId: 'DEMO-002', technicianName: 'Kỹ thuật viên demo B', surveyCount: 1, csat: { averageScore: 4.0 }, nps: { score: null, status: 'demo-unavailable' }, isDemo: true },
];

export default function TechnicianReportPage() {
  const [filters, setFilters] = useState({ startDate: '', endDate: '' }); 
  const [applied, setApplied] = useState(filters);
  const [items, setItems] = useState([]); 
  const [loading, setLoading] = useState(true); 
  const [error, setError] = useState(''); 
  const [showDemo, setShowDemo] = useState(false);

  const load = useCallback(async () => {
    setLoading(true);
    setError('');
    try {
      const result = await getTechnicians(applied);
      setItems(result.items || []);
    } catch (e) {
      setError(e.message);
      setItems([]);
    } finally {
      setLoading(false);
    }
  }, [applied]);

  useEffect(() => {
    load();
  }, [load]);

  const apply = () => {
    if (!filters.startDate || !filters.endDate) {
      setError('Vui lòng chọn khoảng ngày.');
      return;
    }
    if (filters.startDate > filters.endDate) {
      setError('Từ ngày không được sau Đến ngày.');
      return;
    }
    setApplied(filters);
  };

  const reset = () => {
    const empty = { startDate: '', endDate: '' };
    setFilters(empty);
    setApplied(empty);
    setShowDemo(false);
  };

  const rows = showDemo ? [...items, ...DEMO] : items;

  return (
    <section className="page">
      <div className="filter-card">
        <div className="two-col">
          <label>
            Từ ngày
            <input 
              type="date" 
              value={filters.startDate} 
              onChange={e => setFilters({ ...filters, startDate: e.target.value })} 
            />
          </label>
          <label>
            Đến ngày
            <input 
              type="date" 
              value={filters.endDate} 
              onChange={e => setFilters({ ...filters, endDate: e.target.value })} 
            />
          </label>
        </div>
        <label>
          Kỹ thuật viên
          <select value="" onChange={() => {}}>
            <option value="">Tất cả kỹ thuật viên</option>
            {items.map(x => (
              <option key={x.technicianId} value={x.technicianId}>
                {x.technicianName}
              </option>
            ))}
          </select>
        </label>
        <div className="actions">
          <button className="secondary" onClick={reset}>ĐẶT LẠI</button>
          <button onClick={apply}>TÌM KIẾM</button>
        </div>
      </div>

      <div className="demo-control">
        <label>
          <input 
            type="checkbox" 
            checked={showDemo} 
            onChange={e => setShowDemo(e.target.checked)} 
          /> 
          Hiển thị tối đa 2 bản ghi DEMO (không phải dữ liệu thật)
        </label>
      </div>

      <DataState loading={loading} error={error} isEmpty={rows.length === 0} onRetry={load}>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Kỹ thuật viên</th>
                <th>CSAT</th>
                <th>NPS</th>
                <th>Số phiếu</th>
                <th>Nguồn</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r, i) => (
                <tr key={`${r.technicianId}-${i}`}>
                  <td>{r.technicianName}</td>
                  <td>{r.csat?.averageScore == null ? '—' : Number(r.csat.averageScore).toFixed(2)}</td>
                  <td>{r.nps?.score == null ? '—' : r.nps.score}</td>
                  <td>{r.surveyCount ?? 0}</td>
                  <td>{r.isDemo ? <span className="demo-tag">DEMO</span> : 'PostgreSQL/API'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </DataState>

      <p className="hint">
        Chi tiết phiếu cần mã khảo sát cụ thể. API Contract hiện chưa quy định API trả danh sách chi tiết theo kỹ thuật viên.
      </p>
      <Link className="button-link" to="/surveys/1">
        Mở trang chi tiết khảo sát (mẫu ID 1)
      </Link>
    </section>
  );
}
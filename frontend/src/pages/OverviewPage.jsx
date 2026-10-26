import React from 'react';
import { useCallback, useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer, Legend } from 'recharts';
import DataState from '../components/DataState.jsx';
import { getCenters, getSummary, getTrend } from '../api/reportApi.js';

const initial = { startDate: '', endDate: '', centerId: '' };

export default function OverviewPage() {
  const [filters, setFilters] = useState(initial);
  const [applied, setApplied] = useState(initial);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [summary, setSummary] = useState(null);
  const [trend, setTrend] = useState([]);
  const [centers, setCenters] = useState([]);

  const load = useCallback(async () => {
    setLoading(true); 
    setError('');
    try {
      const params = { 
        startDate: applied.startDate, 
        endDate: applied.endDate 
      };

      const reportParams = {
        ...params,
        centerId: applied.centerId,
      };

      const [s, t, c] = await Promise.all([
        getSummary(reportParams), 
        getTrend({ ...reportParams, groupBy: 'day' }), 
        getCenters(params)
      ]);

      setSummary(s); 
      setTrend(t.items || []); 
      setCenters(c.items || []);
    } catch (e) { 
      setError(e.message); 
      setSummary(null); 
      setTrend([]); 
    } finally { 
      setLoading(false); 
    }
  }, [applied]);

  useEffect(() => { 
    load(); 
  }, [load]);

  const apply = () => {
    if (!filters.startDate || !filters.endDate) { 
      setError('Vui lòng chọn Từ ngày và Đến ngày.'); 
      return; 
    }
    if (filters.startDate > filters.endDate) { 
      setError('Từ ngày không được sau Đến ngày.'); 
      return; 
    }
    setApplied(filters);
  };

  const reset = () => { 
    setFilters(initial); 
    setApplied(initial); 
  };

  const count = summary?.surveyCount;
  const csat = summary?.csat?.averageScore;
  const nps = summary?.nps?.score;

  return (
    <section className="page">
      <div className="filter-card">
        <div className="two-col">
          <label>
            Từ ngày
            <input type="date" value={filters.startDate} onChange={e => setFilters({ ...filters, startDate: e.target.value })} />
          </label>
          <label>
            Đến ngày
            <input type="date" value={filters.endDate} onChange={e => setFilters({ ...filters, endDate: e.target.value })} />
          </label>
        </div>
        <label>
          Trung tâm
          <select value={filters.centerId} onChange={e => setFilters({ ...filters, centerId: e.target.value })}>
            <option value="">Tất cả trung tâm</option>
            {centers.map(c => (
              <option key={c.centerId} value={c.centerId}>
                {c.centerName}
              </option>
            ))}
          </select>
        </label>
        <div className="actions">
          <button className="secondary" onClick={reset}>ĐẶT LẠI</button>
          <button onClick={apply}>LỌC BÁO CÁO</button>
        </div>
      </div>

      <DataState loading={loading} error={error} isEmpty={!!summary && Number(count) === 0} onRetry={load}>
        <div className="kpis">
          <Metric title="CSAT" value={csat == null ? '—' : Number(csat).toFixed(2)} note="Thang 1–5" />
          <Metric title="NPS" value={nps == null ? '—' : nps} note={summary?.nps?.status === 'unavailable' ? 'Chưa có dữ liệu NPS hợp lệ' : 'Thang 1 đến 10'} />
          <Metric title="SỐ PHIẾU" value={count ?? '—'} note="Phản hồi hợp lệ" />
        </div>
        <div className="chart-card">
          <h3>Biểu đồ CSAT/NPS theo thời gian</h3>
          {trend.length ? (
            <ResponsiveContainer width="100%" height={280}>
              <LineChart data={trend}>
                <CartesianGrid strokeDasharray="3 3" stroke="#343434" />
                <XAxis dataKey="period" stroke="#b7b7b7" />
                <YAxis yAxisId="csat" domain={[0, 5]} stroke="#b7b7b7" />
                <Tooltip contentStyle={{ background: '#171717', border: '1px solid #555' }} />
                <Legend />
                <Line yAxisId="csat" type="monotone" dataKey="csat.averageScore" name="CSAT" stroke="#26a8ff" connectNulls={false} />
              </LineChart>
            </ResponsiveContainer>
          ) : (
            <div className="chart-empty">
              Khu vực hiển thị biểu đồ<br />
              <small>Chưa có chuỗi dữ liệu để vẽ</small>
            </div>
          )}
        </div>
      </DataState>
    </section>
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
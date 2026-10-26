const BASE_URL = (
  import.meta.env.VITE_API_BASE_URL ||
  'http://127.0.0.1:5000'
).replace(/\/+$/, '');

async function get(path, params = {}) {
  const query = new URLSearchParams();
  
  // Chỉ đưa lên các tham số thực sự có giá trị và không phải placeholder ngày tháng
  Object.entries(params).forEach(([key, value]) => {
    if (
      value !== undefined && 
      value !== null && 
      value !== '' && 
      value !== 'mm/dd/yyyy' && 
      value !== 'all'
    ) {
      query.set(key, String(value));
    }
  });

  const suffix = query.toString() ? `?${query.toString()}` : '';
  const response = await fetch(`${BASE_URL}${path}${suffix}`, { 
    headers: { Accept: 'application/json' } 
  });
  
  const body = await response.json().catch(() => null);
  if (!response.ok) {
    throw new Error(body?.message || body?.error || `API trả về HTTP ${response.status}`);
  }
  return body?.data ?? body;
}

export const getSummary = (params) => get('/api/v1/reports/csat-nps/summary', params);
export const getTrend = (params) => get('/api/v1/reports/csat-nps/trend', params);
export const getCenters = (params) => get('/api/v1/reports/csat-nps/centers', params);
export const getTechnicians = (params) => get('/api/v1/reports/csat-nps/technicians', params);
export const getSurvey = (responseId) => get(`/api/surveys/${encodeURIComponent(responseId)}`);
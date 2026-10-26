
import React from "react";

export default function DataState({
  loading,
  error,
  isEmpty,
  onRetry,
  children,
}) {
  if (loading) {
    return (
      <div className="state" role="status" aria-live="polite">
        Đang tải dữ liệu...
      </div>
    );
  }

  if (error) {
    return (
      <div className="state state-error" role="alert">
        <strong>Không thể tải dữ liệu.</strong>
        <p>{error}</p>
        <button type="button" onClick={onRetry}>
          Thử lại
        </button>
      </div>
    );
  }

  if (isEmpty) {
    return (
      <div className="state" role="status">
        Không có dữ liệu khảo sát phù hợp.
      </div>
    );
  }

  return <>{children}</>;
}

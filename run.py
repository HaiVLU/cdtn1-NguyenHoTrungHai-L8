import io
import logging
import sys

# Ép buộc toàn bộ luồng xuất (stdout/stderr) của Python dùng UTF-8 trên Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# Cấu hình logging mặc định của Python sử dụng UTF-8 để tránh lỗi charmap khi ghi log tiếng Việt
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

from src import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
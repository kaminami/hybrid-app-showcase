from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import threading
import uvicorn

app_port = 8910  # ポート番号を指定（必要に応じて変更）
app = FastAPI()

# APIエンドポイントの例
@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI"}

# 静的ファイルの提供
# APIエンドポイント定義の後に設定する
app.mount("/", StaticFiles(directory="webapp", html=True), name="static")

# サーバー起動
def start_server():
    uvicorn.run(app, host="127.0.0.1", port=app_port, log_level="info")

def start_server_thread():
    threading.Thread(target=start_server, daemon=True).start()


if __name__ == "__main__":
    start_server()

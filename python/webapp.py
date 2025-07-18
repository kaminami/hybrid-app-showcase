from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import threading
import uvicorn

app_port = 8910  # ポート番号を指定（必要に応じて変更）
app = FastAPI()
app.mount("/", StaticFiles(directory="webapp", html=True), name="static")


# APIエンドポイントの例
@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI"}


# サーバー起動
def start_server():
    threading.Thread(target=do_start_server, daemon=True).start()

def do_start_server():
    uvicorn.run(app, host="127.0.0.1", port=app_port, log_level="info")


if __name__ == "__main__":
    start_server()

    # ↓ ここで、UI起動（Electron / WebView / Qt etc.）
    # 例：os.system("electron .")、または Qt GUI の mainloop を起動
    import time
    print("Server started. Keep running...")
    while True:
        time.sleep(1)

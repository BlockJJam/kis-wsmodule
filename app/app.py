from pathlib import Path
from fastapi import FastAPI
import sys

BASE_DIR = Path(__file__).resolve()
sys.path.append(str(BASE_DIR))

def create_app() -> FastAPI:
    app = FastAPI()
    # app.include_router(api.live_router, prefix='/ws')

    return app

app = create_app()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', ws_ping_interval=5, ws_ping_timeout=5, log_level='debug')

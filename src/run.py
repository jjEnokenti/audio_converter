import uvicorn

from src.routes.handlers import app

if __name__ == '__main__':
    uvicorn.run(app, port=5000)

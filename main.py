import uvicorn

from routers import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
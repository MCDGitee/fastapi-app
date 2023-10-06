from fastapi import FastAPI
import uvicorn
from dotenv import dotenv_values

config = dotenv_values(".env")
env_secret_key = config["ENV_SECRET_KEY"]

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello from FastAPI!"}

@app.get("/env")
async def read_env():
    return {"message": f"environment variable = {env_secret_key}"}


if __name__ == '__main__': #this indicates that this a script to be run
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload = True)

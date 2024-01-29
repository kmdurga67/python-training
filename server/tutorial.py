from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/hello")
def hello_world():
    return "World"


@app.post("/receive_data")
async def receive_data(data: dict, variable1: str, variable2: int):
    return {"received_data": data, "variable1": variable1, "variable2": variable2}

if __name__ == "__main__":
    uvicorn.run("tutorial:app", host="127.0.0.1", port=8000, reload=True)

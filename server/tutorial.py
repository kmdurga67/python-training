from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()


@app.get("/hello")
def hello_world():
    return "World"


@app.post("/receive_data")
async def receive_data(data: dict, variable1: str, variable2: int):
    return {"received_data": data, "variable1": variable1, "variable2": variable2}

data = {
    1: "durga"
}


@app.get("/get_data")
async def get_data():
    return {"data": data}


@app.post("/add_data")
async def add_data(item: str):
    new_key = max(data.keys()) + 1
    data[new_key] = item
    return {"message": "Data added successfully", "data": data}


@app.put("/update_data/{item_id}")
async def update_data(item_id: int, updated_item: str):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    data[item_id] = updated_item
    return {"data": data[item_id]}

if __name__ == "__main__":
    uvicorn.run("tutorial:app", host="127.0.0.1", port=8000, reload=True)

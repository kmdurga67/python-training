from fastapi import FastAPI
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
    return {"message": "Data added successfully", new_key: data[new_key]}


@app.put("/update_data/{item_id}")
async def update_data(item_id: int, updated_item: str):
    if item_id not in data:
        return {"message": "Data Not Found"}
    else:
        data[item_id] = updated_item
        return {"message": f"{item_id} updated successfully", item_id: data[item_id]}


@app.delete("/delete_data/{item_id}")
async def delete_data(item_id: int):
    if item_id not in data:
        return {"message": "Data Not Found"}
    else:
        deleted_item = data.pop(item_id)
        return {"message": f"{item_id} deleted successfully", "deleted_item": deleted_item}


if __name__ == "__main__":
    uvicorn.run("tutorial:app", host="127.0.0.1", port=8000, reload=True)

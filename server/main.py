import uvicorn

from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def post_message():
    return {"Hello": "Posting message"}


@app.put("/put")
def put_message():
    return {"Hello": "Get message using put"}


@app.get("/items")
def list_items():
    return {"Hello": "list item route"}


@app.get("/items/{item_id}")
def get_items(item_id: int):
    return {"Items": item_id}


@app.get("/hello")
def get_message():
    return "World"


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "Vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
def get_foods(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "You are healthy"}

    if food_name.value == "fruits":
        return {"food_name": food_name, "message": "You are still healthy, but like sweet things"}

    return {"food_name": food_name, "message": "I like chocolate milk"}


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "New"}]


@app.get("/items")
def list_items_db(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# @app.get("/items/{items_id}")
# def get_items_db(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id, "q": q}

@app.get("/items/{items_id}")
def get_items_db(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({
            "description": "lorem ipsum"
        })
    return item


class Item(BaseModel):
    name: str
    description: str | None = None
    price: int
    tax: float | None = None


@app.post("/items")
def create_items(items: Item):
    item_dict = items.dict()
    if items.tax:
        price_with_tax = items.price + items.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{items_id}")
def update_items(items_id: int, items: Item):
    return ({"items_id": items_id, **items.dict()})


# if __name__ == "__main__":   #dunder
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

    # create API /hello
    # dictionary to post data to particular id

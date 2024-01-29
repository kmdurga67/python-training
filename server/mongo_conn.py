import uvicorn
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import json_util
import json

app = FastAPI()


def connect_to_mongodb():
    try:
        mongo_uri = "mongodb://localhost:27017"
        database_name = "schoolDB"
        collection_name = "students"

        client = MongoClient(mongo_uri)
        db = client[database_name]
        collection = db[collection_name]
        print("Connected to MongoDB")
        return collection

    except Exception as e:
        print(f"Failed to connect to MongoDB. Error: {e}")
        raise


def jsonable_encoder_custom(item):
    return json.loads(json_util.dumps(item))


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = connect_to_mongodb()


@app.get("/get_data")
async def get_data():
    try:
        documents = app.mongodb_client.find()

        result = [jsonable_encoder_custom(doc) for doc in documents]

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

if __name__ == "__main__":
    uvicorn.run("mongo_conn:app", host="127.0.0.1", port=8000)

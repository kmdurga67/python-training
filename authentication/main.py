from datetime import datetime, timedelta
import sqlite3
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import jwt

app = FastAPI()

SECRET_KEY = "b52adf3bb0f9f88033d2f46b20024bae"


class Authenticate(BaseModel):
    id: int
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


conn = sqlite3.connect('auth.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS auth
                  (id INTEGER PRIMARY KEY, password TEXT)''')
conn.commit()


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@app.post("/send-data", tags=["Send Data to Signup"])
async def send_data(user: Authenticate):
    cursor.execute('''INSERT INTO auth (id, password) VALUES (?, ?)''',
                   (user.id, user.password))
    conn.commit()
    return {"message": "Data sent successfully"}


@app.post("/login", response_model=Token, tags=["Authenticate Data to Login"])
async def login(user: Authenticate):
    cursor.execute('''SELECT id, password FROM auth WHERE id=?''',
                   (user.id,))
    result = cursor.fetchone()
    if result:
        stored_password = result[1]
        if user.password == stored_password:
            access_token = create_access_token(data={"id": user.id})
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise HTTPException(
                status_code=401, detail="Either ID or password is wrong")
    else:
        raise HTTPException(status_code=401, detail="Login failed")


@app.get("/protected-route", tags=["Protected Route"])
async def protected_route(token: str = Depends(verify_token)):
    return {"message": "This is a protected route", "user_id": token["id"]}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

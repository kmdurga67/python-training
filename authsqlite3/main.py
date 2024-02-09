import sqlite3
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Authenticate(BaseModel):
    id: int
    password: str


conn = sqlite3.connect('auth.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS auth
                  (id INTEGER PRIMARY KEY, password TEXT)''')
conn.commit()


@app.post("/send-data", tags=["Send Data to Signup"])
async def send_data(user: Authenticate):
    cursor.execute('''INSERT INTO auth (id, password) VALUES (?, ?)''',
                   (user.id, user.password))
    conn.commit()
    return {"message": "Data sent successfully"}


@app.post("/check-login", tags=["Authenticate Data to Login"])
async def check_login(user: Authenticate):
    cursor.execute('''SELECT id, password FROM auth WHERE id=?''',
                   (user.id,))
    result = cursor.fetchone()
    if result:
        stored_password = result[1]
        if user.password == stored_password:
            return {"message": "Login successful"}
        else:
            raise HTTPException(
                status_code=401, detail="Either ID or password is wrong")
    else:
        raise HTTPException(status_code=401, detail="Login failed")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

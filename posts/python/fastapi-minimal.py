"""
Api minima com fastAPI

Dependencias:

>> pip3 install fastapi
>> pip3 install uvicorn

Executando:

>> uvicorn server:app 

server.py:
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!"}

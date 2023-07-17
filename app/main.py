from fastapi import FastAPI
from .model.request import Request


app = FastAPI()


@app.post("/execute/python")
async def root(request: Request):
   return {"message": "Hello World"}
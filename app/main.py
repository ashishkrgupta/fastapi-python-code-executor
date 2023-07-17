from fastapi import FastAPI
from .model.request import Request
from .model.response import Response


app = FastAPI()


@app.post("/execute/python")
async def root(request: Request):
   resp = Response()
   return resp
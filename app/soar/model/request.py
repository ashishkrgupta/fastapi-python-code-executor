from pydantic import BaseModel, Field
from .onPremNode import OnPremNode
from .codeRequest import CodeRequest


class Request(BaseModel):
    id:str
    requestId:str = Field(None, title="the unique id to corelate the response")
    customCodeRequest: CodeRequest
    onpremnode: OnPremNode
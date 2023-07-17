from pydantic import BaseModel
from .codeResponse import CodeResponse


class Response(BaseModel):
    id:str = None
    customCodeResponse: CodeResponse = None
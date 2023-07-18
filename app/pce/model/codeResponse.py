from pydantic import BaseModel
from .request import Request

class CodeResponse(BaseModel):
    language:str = None
    requestId:str = None
    status:str = None
    message:str = None
    input:dict = None
    output:dict = None
    

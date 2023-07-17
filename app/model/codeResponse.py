from pydantic import BaseModel

class CodeResponse(BaseModel):
    language:str
    requestId:str
    status:str
    message:str
    input:dict
    output:dict
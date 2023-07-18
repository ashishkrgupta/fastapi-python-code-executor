from pydantic import BaseModel

class OnPremNode(BaseModel):
    subscriptionId:str
    id:int
    name:str
    tenantId:int
    tenantName:str
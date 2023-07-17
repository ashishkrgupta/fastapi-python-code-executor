from fastapi import FastAPI
from .model.request import Request
from .model.response import Response
from .model.codeResponse import CodeResponse
from .model.codeRequest import CodeRequest
import uuid
import os
import logging
from importlib.machinery import SourceFileLoader



logging.basicConfig(filename = 'app.log', level = logging.INFO, format = '%(levelname)s:%(asctime)s:%(message)s')


app = FastAPI()


@app.post("/execute/python")
async def root(request: Request):
   resp = Response()
   resp.customCodeResponse = CodeResponse()
   resp.customCodeResponse.input = request.customCodeRequest
   resp.customCodeResponse.language = request.customCodeRequest.language
   resp.customCodeResponse.requestId = request.requestId
   
   try:
      logging.info("invoked %s", "/execute/python")
      absFile = getPythonFile(request.customCodeRequest.code)
      logging.info("script file created by name %s", absFile)
      # code to execute file
      logging.debug("Executing python script")
      executeScript(absFile, request.customCodeRequest, resp.customCodeResponse)
      
      # delete the creaed python file
      logging.info("Python script execution completed, deleting script file")
      os.remove(absFile)
      logging.info("script file deleted")
   except Exception as ex:
      logging.error("Exception while executing cusome code %s", ex)
      resp.customCodeResponse.status = "Failed"
      resp.customCodeResponse.message = str(ex)
   return resp

def executeScript(scriptPath: str, codeReq: CodeRequest, codeResp: CodeResponse):
   module_name=scriptPath.split("/")[-1].split(".")[0]
   load_module = SourceFileLoader(module_name, scriptPath).load_module()
   method = getattr(load_module, codeReq.invokefunction)
   result = method(*codeReq.input)
   codeResp.output = result
   codeResp.message = "Execution Successful"
   codeResp.status = "success"

def getPythonFile(code: str):
   createScriptsFolder()
   filename = "scripts/" + str(uuid.uuid4()) + ".py"
   file = open(filename, 'a')
   file.write(code)
   file.close()
   return os.path.abspath(filename)


def createScriptsFolder():
   if not os.path.exists("scripts"):
      os.mkdir("scripts")
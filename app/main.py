from fastapi import FastAPI
from .model.request import Request
from .model.response import Response
from .model.codeResponse import CodeResponse
from .model.codeRequest import CodeRequest
import uuid
import os
import logging
from multiprocessing import Process


logging.basicConfig(filename = 'app.log', level = logging.INFO, format = '%(levelname)s:%(asctime)s:%(message)s')


app = FastAPI()


@app.post("/execute/python")
async def root(request: Request):
   resp = Response()
   logging.info("invoked %s", "/execute/python")
   absFile = getPythonFile(request.customCodeRequest.code)
   logging.info("script file created by name %s", absFile)
   # code to execute file
   logging.debug("Executing python script")
   resp.customCodeResponse = executeScript(absFile, request.customCodeRequest)
   resp.customCodeResponse.input = request.customCodeRequest
   resp.customCodeResponse.language = request.customCodeRequest.language
   resp.customCodeResponse.requestId = request.requestId
   
   
   # delete the creaed python file
   logging.info("Python script execution completed, deleting script file")
   os.remove(absFile)
   logging.info("script file deleted")
   return resp

def executeScript(scriptPath: str, codeReq:CodeRequest):
   resp = CodeResponse()
   resp.message = "Execution Successful"
   resp.status = "success"
   
   p = Process(target = codeReq.invokefunction, args = codeReq.input)
   p.start()
   p.join() # this blocks until the process terminates
   
   print(p)
   
   resp.output = {}
   return resp

def getPythonFile(code: str):
   createScriptsFolder();
   filename = "scripts/" + str(uuid.uuid4()) + ".py"
   file = open(filename, 'a')
   file.write(code)
   file.close()
   
   # temp code
   f = open(filename, "r")
   print(f.read())
   return os.path.abspath(filename)

def createScriptsFolder():
   if not os.path.exists("scripts"):
      os.mkdir("scripts")
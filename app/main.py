from fastapi import FastAPI
import logging
from .pce.model.request import Request
from .pce.model.response import Response
from .pce.model.codeResponse import CodeResponse
from .pce.service.codeExecutionService import CodeExecutionService
from .pce.service.codeFileService import CodeFileService

logging.basicConfig(filename = 'app.log', level = logging.INFO, format = '%(levelname)s:%(asctime)s:%(message)s')

app = FastAPI()

@app.post("/execute/python")
async def root(request: Request):
   resp = Response()
   resp.customCodeResponse = CodeResponse()
   resp.customCodeResponse.input = request.customCodeRequest.__dict__
   resp.customCodeResponse.language = request.customCodeRequest.language
   resp.customCodeResponse.requestId = request.requestId
   codeFile = CodeFileService()
   absFile = ""
   try:
      logging.info("invoked %s", "/execute/python")
      absFile = codeFile.getPythonFile(request.customCodeRequest.code)
      logging.info("script file created by name %s", absFile)
      # code to execute file
      logging.debug("Executing python script")
      exeService = CodeExecutionService()
      exeService.executeScript(absFile, request.customCodeRequest, resp.customCodeResponse)
      logging.info("Python script execution completed")
   except Exception as ex:
      logging.error("Exception while executing cusome code %s", ex)
      resp.customCodeResponse.status = "Failed"
      resp.customCodeResponse.message = str(ex)
   finally:
      codeFile.removeFile(absFile)
   return resp


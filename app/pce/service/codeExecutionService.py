from ..model.codeRequest import CodeRequest
from ..model.codeResponse import CodeResponse
from importlib.machinery import SourceFileLoader
from ..util.scriptUtil import ScriptUtil

class CodeExecutionService:
    
    def executeScript(self, scriptPath: str, codeReq: CodeRequest, codeResp: CodeResponse):
        module_name = scriptPath.split("/")[-1].split(".")[0]
        module = SourceFileLoader(module_name, scriptPath).load_module()
        scriptUtil = ScriptUtil()
        imports = scriptUtil.find_imports(open(scriptPath).read())
        print(imports)
        method = getattr(module, codeReq.invokefunction)
        result = method(*codeReq.input)
        codeResp.output = result
        codeResp.message = "Execution Successful"
        codeResp.status = "success"
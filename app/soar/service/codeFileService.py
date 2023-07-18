import uuid
import os
import logging

logging.basicConfig(filename = 'app.log', level = logging.INFO, format = '%(levelname)s:%(asctime)s:%(message)s')
SCRIPTS_FOLDER = "scripts"

class CodeFileService:
    
    def getPythonFile(self, code: str):
        self.createScriptsFolder()
        filename = SCRIPTS_FOLDER + "/" + str(uuid.uuid4()) + ".py"
        file = open(filename, 'a')
        file.write(code)
        file.close()
        return os.path.abspath(filename)
    
    def createScriptsFolder(self):
        if not os.path.exists(SCRIPTS_FOLDER):
            os.mkdir(SCRIPTS_FOLDER)
            
    def removeFile(self, absFile: str):
        if os.path.exists(absFile):
            os.remove(absFile)
            logging.info("script file %s deleted", absFile)


class ScriptUtil:
    
    def find_imports(self, code: str):
        modules = []
        code = code.splitlines()
        for item in code:
            if item[:7] == "import " and ", " not in item:
                if " as " in item:
                    modules.append(item[7:item.find(" as ")])
                else:
                    modules.append(item[7:])
            elif item[:5] == "from ":
                modules.append(item[5:item.find(" import ")])
            elif ", " in item:
                item = item[7:].split(", ")
                modules = modules+item
        return modules
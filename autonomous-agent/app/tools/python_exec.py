from .base import BaseTool

class PythonTool(BaseTool):
    name = "python_executor"
    description = "Execute Python code."

    def run(self, input: str) -> str:
        try:
            local_env = {}
            exec(input, {}, local_env)
            return str(local_env)
        except Exception as e:
            return f"Execution error: {str(e)}"
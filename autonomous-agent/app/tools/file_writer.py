from .base import BaseTool

class FileWriterTool(BaseTool):
    name = "file_writer"
    description = "Write content to a local file."

    def run(self, input: str) -> str:
        try:
            filename, content = input.split("||", 1)
            with open(filename.strip(), "w") as f:
                f.write(content.strip())
            return "File written successfully."
        except Exception as e:
            return f"File error: {str(e)}"
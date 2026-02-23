from duckduckgo_search import DDGS
from .base import BaseTool

class SearchTool(BaseTool):
    name = "web_search"
    description = "Search the web for recent information."

    def run(self, input: str) -> str:
        with DDGS() as ddgs:
            results = ddgs.text(input, max_results=3)
            output = "\n".join([r["body"] for r in results])
        return output[:2000]  # truncate to avoid context overflow
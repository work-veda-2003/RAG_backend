from app.agent import AutonomousAgent
from app.memory import ShortTermMemory
from app.tools.search import SearchTool
from app.tools.python_exec import PythonTool
from app.tools.file_writer import FileWriterTool

def main():
    tools = [SearchTool(), PythonTool(), FileWriterTool()]
    memory = ShortTermMemory()
    agent = AutonomousAgent(tools, memory)

    task = input("Enter task: ")
    result = agent.run(task)
    print("Final Output:\n", result)

if __name__ == "__main__":
    main()
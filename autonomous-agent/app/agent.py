import ollama
import json
import re
from app.prompts import SYSTEM_PROMPT
from app.utils import MAX_ITERATIONS


class AutonomousAgent:
    def __init__(self, tools, memory):
        self.tools = {t.name: t for t in tools}
        self.memory = memory

    def extract_json(self, text):
        try:
            # Extract JSON block using regex
            match = re.search(r"\{.*\}", text, re.DOTALL)
            if match:
                return json.loads(match.group())
        except:
            return None
        return None

    def run(self, task: str):
        self.memory.add("user", task)

        for step in range(MAX_ITERATIONS):
            print(f"\nStep {step+1} reasoning...")

            response = ollama.chat(
                model="llama3",
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] + self.memory.get()
            )

            content = response["message"]["content"]
            print("Raw model output:\n", content)

            parsed = self.extract_json(content)

            if not parsed:
                print("Could not parse JSON. Retrying...")
                continue

            thought = parsed.get("thought")
            action = parsed.get("action")
            action_input = parsed.get("action_input")
            final_answer = parsed.get("final_answer")

            print("Thought:", thought)
            print("Action:", action)

            self.memory.add("assistant", content)

            if action == "finish":
                return final_answer

            if action in self.tools:
                tool_result = self.tools[action].run(action_input)
                print("Tool result:", tool_result)
                self.memory.add("tool", tool_result)
            else:
                return "Invalid tool selected."

        return "Stopped due to iteration limit."
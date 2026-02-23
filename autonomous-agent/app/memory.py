class ShortTermMemory:
    def __init__(self, max_messages=6):
        self.max_messages = max_messages
        self.messages = []

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get(self):
        return self.messages
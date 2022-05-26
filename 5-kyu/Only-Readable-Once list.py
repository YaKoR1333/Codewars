class SecureList():
    def __init__(self, messages):
        self.messages = [item for item in messages]

    def __getitem__(self, key):
        val = self.messages[key]
        self.messages.pop(key)
        return val

    def __str__(self):
        messages = self.messages
        self.messages = []
        return str(messages)

    def __repr__(self):
        messages = self.messages
        self.messages = []
        return str(messages)

    def __len__(self):
        return len(self.messages)

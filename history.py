class History:
    def __init__(self):
        self._entries = []

    def add(self, expression, result):
        self._entries.append((expression, result))

    def show(self, n=10):
        return self._entries[-n:]

    def clear(self):
        self._entries.clear()

    def __len__(self):
        return len(self._entries)

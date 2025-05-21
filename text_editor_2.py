class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    undo_stack = Stack()

    print("Typing 'Hello'")
    undo_stack.push("Type: Hello")
    print("Typing ' World'")
    undo_stack.push("Type:  World")
    print("Deleting last character")
    undo_stack.push("Delete: d")

    print("\nCurrent undo stack (top to bottom):", list(reversed(undo_stack.items)))

    print("\nPerforming Undo:")
    last_action = undo_stack.pop()
    print(f"Undo action: {last_action}")
    print("Current undo stack:", list(reversed(undo_stack.items)))

    last_action = undo_stack.pop()
    print(f"Undo action: {last_action}")
    print("Current undo stack:", list(reversed(undo_stack.items)))

    print("\nAdding new action:")
    undo_stack.push("Type: !")
    print("Current undo stack:", list(reversed(undo_stack.items)))
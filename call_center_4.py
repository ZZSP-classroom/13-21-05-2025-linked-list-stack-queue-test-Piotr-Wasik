import datetime

class Call:
    def __init__(self, caller_id):
        self.caller_id = caller_id
        self.time_received = datetime.datetime.now()

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

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
    incoming_calls = Queue()
    processed_calls = Stack()

    print("Incoming Call: 101")
    call1 = Call("101")
    incoming_calls.enqueue(call1)
    print("Incoming Call: 102")
    call2 = Call("102")
    incoming_calls.enqueue(call2)
    print("Incoming Call: 103")
    call3 = Call("103")
    incoming_calls.enqueue(call3)

    print("\nIncoming Queue (call IDs):")
    for call in incoming_calls.items:
        print(f"  {call.caller_id} received at {call.time_received.strftime('%H:%M:%S')}")

    print("\nProcessing Calls:")
    while not incoming_calls.is_empty():
        call = incoming_calls.dequeue()
        if call:
            print(f"Processing call ID: {call.caller_id}")
            processed_calls.push(call)

    print("\nCalls currently being processed (stack top is last processed call ID):")
    for call in reversed(processed_calls.items): # Display top to bottom
        print(f"  {call.caller_id} received at {call.time_received.strftime('%H:%M:%S')}")


    print("\nAgent finishes call:")
    finished_call = processed_calls.pop()
    if finished_call:
        print(f"Finished processing call ID: {finished_call.caller_id}")

    print("Calls remaining in process (call IDs):")
    for call in reversed(processed_calls.items):
        print(f"  {call.caller_id} received at {call.time_received.strftime('%H:%M:%S')}")

    print("\nNew incoming call: 104")
    call4 = Call("104")
    incoming_calls.enqueue(call4)
    print("Incoming Queue (call IDs):")
    for call in incoming_calls.items:
        print(f"  {call.caller_id} received at {call.time_received.strftime('%H:%M:%S')}")
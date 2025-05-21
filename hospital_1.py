class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time

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


q = Queue()
p1 = Patient("Alice", "10:00 AM")
p2 = Patient("Bob", "10:15 AM")
p3 = Patient("Charlie", "10:30 AM")

q.enqueue(p1)
q.enqueue(p2)
q.enqueue(p3)

print("Current queue (patient objects):", q.items)
print("Next patient (object):", q.peek())
if q.peek():
    print(f"Next patient name: {q.peek().name}")

dequeued_patient = q.dequeue()
print("Dequeue (object):", dequeued_patient)
if dequeued_patient:
    print(f"Dequeued patient name: {dequeued_patient.name}")
print("Current queue (patient objects):", q.items)
if q.peek():
    print(f"Next patient name: {q.peek().name}")

q.dequeue()
q.dequeue()
print("Is queue empty?", q.is_empty())
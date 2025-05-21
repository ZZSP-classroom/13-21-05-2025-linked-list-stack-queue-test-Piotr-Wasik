class Task:
    def __init__(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority    

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.head or task.priority < self.head.task.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and task.priority >= current.next.task.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def process_task(self):
        if not self.is_empty():
            task_to_process = self.head.task
            self.head = self.head.next
            return task_to_process
        return None
    def peek_next_task(self):
        return self.head.task if self.head else None

    def is_empty(self):
        return self.head is None

    def display_tasks(self):
        current = self.head
        tasks_info = []
        while current:
            tasks_info.append(f"({current.task.task_name}, P:{current.task.priority})")
            current = current.next
        print("Tasks in Queue (High Priority First):", " -> ".join(tasks_info) if tasks_info else "Empty")


if __name__ == "__main__":
    pq = PriorityQueue()

    print("Adding tasks:")
    pq.add_task(Task("Urgent Report", 1))
    pq.add_task(Task("Email Replies", 3))
    pq.add_task(Task("Meeting Prep", 2))
    pq.add_task(Task("Coffee Break", 5))
    pq.add_task(Task("Bug Fix", 1))

    pq.display_tasks()

    print("\nProcessing tasks:")
    while not pq.is_empty():
        task = pq.process_task()
        if task:
            print(f"Processing: {task.task_name} (Priority: {task.priority})")
        pq.display_tasks()
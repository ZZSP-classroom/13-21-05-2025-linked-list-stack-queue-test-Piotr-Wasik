import unittest
from task_scheduler_5 import PriorityQueue, Task, Node

class TestTaskScheduler(unittest.TestCase):
    def test_add_task_priority_order(self):
        pq = PriorityQueue()
        task1 = Task("Low Priority", 5)
        task2 = Task("High Priority", 1)
        task3 = Task("Medium Priority", 3)
        task4 = Task("Another High", 1)

        pq.add_task(task1)
        pq.add_task(task3)
        pq.add_task(task2)
        pq.add_task(task4)

        self.assertEqual(pq.process_task(), task2)
        self.assertEqual(pq.process_task(), task4)
        self.assertEqual(pq.process_task(), task3)
        self.assertEqual(pq.process_task(), task1)
        self.assertTrue(pq.is_empty())

    def test_process_task_empty_queue(self):
        pq = PriorityQueue()
        self.assertIsNone(pq.process_task())

    def test_peek_next_task(self):
        pq = PriorityQueue()
        self.assertIsNone(pq.peek_next_task())
        task1 = Task("Task A", 2)
        task2 = Task("Task B", 1)
        pq.add_task(task1)
        self.assertEqual(pq.peek_next_task(), task1)
        pq.add_task(task2)
        self.assertEqual(pq.peek_next_task(), task2)
        pq.process_task()
        self.assertEqual(pq.peek_next_task(), task1)

    def test_is_empty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())
        pq.add_task(Task("Test", 1))
        self.assertFalse(pq.is_empty())
        pq.process_task()
        self.assertTrue(pq.is_empty())

if __name__ == '__main__':
    unittest.main()

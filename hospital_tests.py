import unittest
from hospital_1 import Queue, Patient

class TestHospitalQueue(unittest.TestCase):
    def test_enqueue_order(self):
        q = Queue()
        p1 = Patient("Alice", "10:00 AM")
        p2 = Patient("Bob", "10:15 AM")
        q.enqueue(p1)
        q.enqueue(p2)
        self.assertEqual(q.peek(), p1)
        self.assertEqual(q.items[1], p2)

    def test_dequeue_removes_correct_patient(self):
        q = Queue()
        p1 = Patient("Alice", "10:00 AM")
        p2 = Patient("Bob", "10:15 AM")
        q.enqueue(p1)
        q.enqueue(p2)
        dequeued_patient = q.dequeue()
        self.assertEqual(dequeued_patient, p1)
        self.assertEqual(q.peek(), p2)
        self.assertEqual(q.size(), 1)

    def test_dequeue_empty_queue(self):
        q = Queue()
        self.assertIsNone(q.dequeue())

    def test_peek_empty_queue(self):
        q = Queue()
        self.assertIsNone(q.peek())

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(Patient("Test", "11:00 AM"))
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertTrue(q.is_empty())

if __name__ == '__main__':
    unittest.main()
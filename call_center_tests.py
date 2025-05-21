import unittest
from call_center_4 import Queue, Stack, Call
import datetime

class TestCallCenter(unittest.TestCase):
    def test_incoming_calls_queue(self):
        q = Queue()
        call1 = Call("C1")
        call2 = Call("C2")
        q.enqueue(call1)
        q.enqueue(call2)
        self.assertEqual(q.dequeue(), call1)
        self.assertEqual(q.dequeue(), call2)
        self.assertTrue(q.is_empty())

    def test_processed_calls_stack(self):
        s = Stack()
        call1 = Call("C1")
        call2 = Call("C2")
        s.push(call1)
        s.push(call2)
        self.assertEqual(s.pop(), call2)
        self.assertEqual(s.pop(), call1)
        self.assertTrue(s.is_empty())

    def test_call_flow(self):
        incoming = Queue()
        processing = Stack()

        call1 = Call("C101")
        call2 = Call("C102")
        call3 = Call("C103")

        incoming.enqueue(call1)
        incoming.enqueue(call2)
        incoming.enqueue(call3)

        processing.push(incoming.dequeue())
        processing.push(incoming.dequeue())

        self.assertEqual(incoming.size(), 1)
        self.assertEqual(incoming.peek(), call3)
        self.assertEqual(processing.size(), 2)
        self.assertEqual(processing.peek(), call2)

        
        finished_call = processing.pop()
        self.assertEqual(finished_call, call2)
        self.assertEqual(processing.size(), 1)
        self.assertEqual(processing.peek(), call1)

        call4 = Call("C104")
        incoming.enqueue(call4)
        self.assertEqual(incoming.size(), 2)
        self.assertEqual(incoming.peek(), call3)

if __name__ == '__main__':
    unittest.main()
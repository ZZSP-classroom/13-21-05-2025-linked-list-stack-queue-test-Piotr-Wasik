import unittest
from text_editor_2 import Stack

class TestTextEditorUndo(unittest.TestCase):
    def test_push(self):
        s = Stack()
        s.push("Action 1")
        self.assertEqual(s.peek(), "Action 1")
        s.push("Action 2")
        self.assertEqual(s.peek(), "Action 2")
        self.assertEqual(s.size(), 2)

    def test_pop(self):
        s = Stack()
        s.push("Action 1")
        s.push("Action 2")
        self.assertEqual(s.pop(), "Action 2")
        self.assertEqual(s.peek(), "Action 1")
        self.assertEqual(s.pop(), "Action 1")
        self.assertTrue(s.is_empty())
        self.assertIsNone(s.pop()) 

    def test_peek(self):
        s = Stack()
        self.assertIsNone(s.peek())
        s.push("Action 1")
        self.assertEqual(s.peek(), "Action 1")
        s.push("Action 2")
        self.assertEqual(s.peek(), "Action 2")
        self.assertEqual(s.size(), 2)

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push("Action")
        self.assertFalse(s.is_empty())
        s.pop()
        self.assertTrue(s.is_empty())

if __name__ == '__main__':
    unittest.main()
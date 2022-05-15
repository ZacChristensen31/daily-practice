import unittest

from GeneralAlgorithms.PriorityQueue.priority_queue import PriorityQueue


class MyTestCase(unittest.TestCase):
    def test_insert_priority(self):
        queue = PriorityQueue()
        queue.push('second', 2)
        queue.push('third', 3)
        queue.push('first', 1)

        self.assertEqual(queue.pop(), 'first')
        self.assertEqual(queue.pop(), 'second')
        self.assertEqual(queue.pop(), 'third')

    def test_same_priority(self):
        queue = PriorityQueue()
        queue.push('first', 1)
        queue.push('second', 1)
        queue.push('third', 1)

        self.assertEqual(queue.pop(), 'first')
        self.assertEqual(queue.pop(), 'second')
        self.assertEqual(queue.pop(), 'third')

    def test_top_function(self):
        queue = PriorityQueue()
        queue.push('second', 2)
        queue.push('third', 3)
        queue.push('first', 1)

        self.assertEqual(queue.top(), (1, 2, 'first'))

if __name__ == '__main__':
    unittest.main()

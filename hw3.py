import unittest


class Item:

    def __init__(self, data):
        self.data = data


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()

    def front(self):
        if not self.items:
            res = None
        else:
            res = self.items[-1].data
        return res

    def back(self):
        if not self.items:
            res = None
        else:
            res = self.items[0].data
        return res

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []


class TestQueueMethods(unittest.TestCase):

    def test_enqueue_back_front_size(self):

        item0 = Item(0)
        item1 = Item(1)
        queue_o = Queue()

        queue_o.enqueue(item0)
        queue_o.enqueue(item1)

        self.assertEqual(queue_o.items, [item1, item0])
        self.assertEqual(queue_o.front(), item0.data)
        self.assertEqual(queue_o.back(), item1.data)
        self.assertEqual(queue_o.size(), 2)

    def test_dequeue(self):

        item_l = []
        queue_o = Queue()

        for i in range(4):
            item_l.append(Item(i))
            queue_o.enqueue(item_l[i])

        for j in range(2):
            queue_o.dequeue()

        self.assertEqual(queue_o.items, [item_l[3], item_l[2]])

    def test_clear(self):

        item_l = []
        queue_o = Queue()

        for i in range(4):
            item_l.append(Item(i))
            queue_o.enqueue(item_l[i])

        queue_o.clear()

        self.assertEqual(queue_o.items, [])

    def test_one_element(self):

        queue_o = Queue()
        queue_o.enqueue(Item(1))

        self.assertEqual(queue_o.front(), queue_o.back())

    def test_empty(self):

        queue_o = Queue()
        queue_o.dequeue()

        self.assertEqual(queue_o.items, [])
        self.assertEqual(queue_o.front(), None)
        self.assertEqual(queue_o.back(), None)


t = TestQueueMethods()
t.test_enqueue_back_front_size()
t.test_dequeue()
t.test_clear()
t.test_one_element()
t.test_empty()

# q = Queue()
# i = Item(0)
# q.enqueue(i)

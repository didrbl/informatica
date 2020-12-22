class Item:

    def __init__(self, data):
        self.data = data


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
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


a, b, c = Item(1), Item('cat'), Item('dog')
q = Queue()

for i in [a, b, c]:
    q.enqueue(i)

print(q.front())
print(q.back())

q.dequeue()

print(q.front())
print(q.back())

print(q.size())

q.clear()

print(q.size())

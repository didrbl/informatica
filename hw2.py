class Item:

    def __init__(self, data):
        self.data = data
        self.next = None

        
class Queue:

    def __init__(self):
        self.front = self.back = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, element):
        temp = Item(element)

        if self.back is None:
            self.front = self.back = temp
            return
        self.back.next = temp
        self.back = temp

    def dequeue(self):

        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.back = None

    def size(self):
        count = 0
        item = self.front
        while item:
            count += 1
            item = item.next
        return count
    
    def clear(self):
        while self.front is not None:
            temp = self.front
            self.front = self.front.next
            temp = None

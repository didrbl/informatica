class Item:

    def __init__(self, data):
        self.data = data
        self.next = None


# A class to represent a queue 

# The queue, front stores the front element 
# of LL and back stores the last element of LL 
class Queue:

    def __init__(self):
        self.front = self.back = None

    def is_empty(self):
        return self.front is None

    # Method to add an element to the queue 
    def enqueue(self, element):
        temp = Item(element)

        if self.back is None:
            self.front = self.back = temp
            return
        self.back.next = temp
        self.back = temp

        # Method to remove an element from queue 

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

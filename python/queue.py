class Queue:
    # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
    def __init__(self):
        self.total = 0
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)
        self.total += 1
        return self.queue

    def dequeue(self):
        self.total -= 1
        return self.queue.pop()

    def size(self):
        # write your code that returns the size of the Queue
        return self.total


queue_1 = Queue()
print(queue_1.size())

print(queue_1.enqueue(1))
print(queue_1.enqueue(2))
print(queue_1.enqueue(3))
print(queue_1.size())

print(queue_1.dequeue())
print(queue_1.size())
print(queue_1.queue)

maxSize = 8 # max size of queue

# Queue Class
class Queue:

    # Initialize queue
    def __init__(self):
        self.queue = []

    # Check if queue full
    def isFull(self):
        if len(self) >= maxSize:
            print("Queue is Full!\n")
            return True
        return False

    # Check if queue empty
    def isEmpty(self):
        if len(self.queue) == -1:
            print("Queue is Empty!\n")
            return True
        return False

    # Add element into queue
    def enqueue(self, value):
        if Queue.isFull(self.queue): # check if queue is full
            pass
        else:
            self.queue.append(value)

    # Remove element from queue
    def dequeue(self):
        if Queue.isEmpty(self): # check if queue is empty
            pass
        else:
            self.queue.pop()
            
    # Display queue
    def display(self):
        print("\nQueue: ", self.queue)
        return
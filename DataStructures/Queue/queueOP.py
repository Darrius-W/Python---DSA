# Queue Class
class Queue:

    maxSize = 8 # max size of queue

    # Initialize queue
    def __init__(self):
        self.queue = []

    # Add element into queue
    def enqueue(self, value):
        if len(self.queue) >= self.maxSize: # check if queue is full
            print("\nQueue is Full!")
            pass
        else:
            self.queue.append(value)

    # Remove element from queue
    def dequeue(self):
        if len(self.queue) < 1: # check if queue is empty
            print("\nQueue is Empty!")
            pass
        else:
            self.queue.pop(0)
            
    # Display queue
    def display(self):
        print("\nQueue: ", self.queue)
        return
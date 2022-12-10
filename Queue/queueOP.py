maxSize = 8 # max size of queue

# Queue Class
class Queue:

    # Initialize queue
    def __init__(self):
        self.queue = []

    # Add element into queue
    def enqueue(self, value):
        if len(self.queue) >= maxSize: # check if queue is full
            print("Queue is Full!\n")
            pass
        else:
            self.queue.append(value)

    # Remove element from queue
    def dequeue(self):
        if len(self.queue) < 1: # check if queue is empty
            print("Queue is Empty!\n")
            pass
        else:
            self.queue.pop(0)
            
    # Display queue
    def display(self):
        print("\nQueue: ", self.queue)
        return
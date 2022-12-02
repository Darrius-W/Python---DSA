maxSize = 8 # max size of queue

## Queue Class
class Queue:
    # Initialize queue
    def __init__(self):
        self.queue = []
    # Check if queue full
    def isFull(self):
        if len(self.queue) >= 8:
            print("Queue is Full!\n")
            return True
        return False
    # Check if queue empty
    # Add element into queue
    # Remove element from queue
    # Display queue
# Queue Class - First In First Out(FIFO) structure
# a Linear data structure
'''
Example: a line of people at the bank. The
bank teller will service the first person 
in line, then they will leave the line and
the next person in line will be serviced.
All while people are entering the back of
the line.
'''
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
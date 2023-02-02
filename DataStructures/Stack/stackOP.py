#implementation of a stack in python

class Stack:
    stackMax = 8

    #Initialize Stack
    def __init__(self):
        self.stack = []

    #Check if stack full
    def checkFull(self):
        if len(self.stack) == self.stackMax:
            print("Stack is Full!")
            return True
        else:
            return False
            
    #Push to stack
    def push(self, item):
        if self.checkFull():
            pass
        else:
            self.stack.append(item)
            print("Following item added to stack: ", item)
        
    #Check if stack empty
    def checkEmpty(self):
        if len(self.stack) == 0:
            print("\nStack is empty!\n")
            return True
        else: return False
    
    #Pop from stack
    def pop(self):
        if self.checkEmpty():
            pass
        else:
            self.stack.pop()
    
    #Display stack
    def display(self):
        print("\n", self.stack)
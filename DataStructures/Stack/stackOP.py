# Stack Class - Last In First Out(LIFO) structure
# is a Linear data structure
'''
Exmaple: a stack of books, you have to remove the
each book on top before you can access the book
on the bottom.
'''

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
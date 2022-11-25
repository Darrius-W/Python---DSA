#implementation of a stack in python

import time

stackMax = 10

#Create stack
def createStack():
    stack = []
    return (stack)
    
#Check if stack empty
def checkEmpty(stack):
    if len(stack) == 0:
        return ("Stack is empty!\n")
    

#Check if stack full
def checkFull(stack):
    if len(stack) == stackMax:
        return ("Stack is Full!")
    
#Push to stack
def push(stack, item):
    stack.append(item)
    print("Following item added to stack: ", item)
    
#Pop from stack
def pop(stack):
    if checkEmpty(stack):
        return ("Stack is empty!\n")
    
    stack.pop()
    
#Display stack
def displayStack(stack):
    return print("Result of stack: ", stack)
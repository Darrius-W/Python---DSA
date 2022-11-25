import stackOP
import time

def userInput():
    num = None
    # Collect User num
    try:
        num = int(input())
        
        if (num > 4) or (num < 1):
            raise ValueError("***Erorr Invalid Input***\n")

    except ValueError as ve:
        print(ve)

    return num
        


#Create stack
stack = stackOP.createStack()

op = None

while(op != 4):
    
    #Ask user whether they would like to Pop/Push/Display/Exit
    print("Please select stack operation:\n")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
        
        
    # Collect User Operation
    op = userInput()
            
        # Compare op to Operation
    match op:
        case 1: #PUSH
            print("Enter value you want to add: ")
            stackOP.push(stack, userInput())
            time.sleep(.5)
                
        case 2: #POP
            stackOP.pop(stack)
                
        case 3: #DISPLAY
            print("Result of stack: ", stackOP.displayStack(stack))
            time.sleep(.5)
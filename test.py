import menuOperations as menuOP
import Stack.stackOP as stack

#Create menu obj
menuObj = menuOP.Menu()
stackObj = stack.Stack()

#Menu Options
menuObj.addMenuOp("Push to Stack")
menuObj.addMenuOp("Pop Stack")
menuObj.addMenuOp("Display")

while True:
    
    #Display menu
    menuObj.displayMenu()
    
    #Ask user for input
    userInput = menuObj.requestInput()

    #Find user input and pull function
    match userInput:
        case 1:
            val = int(input("\nEnter integer value: "))
            stackObj.push(val)
    
        case 2:
            stackObj.pop()
        
        case 3:
            stackObj.display()
    
        case default:
            menuObj.exitMenu()
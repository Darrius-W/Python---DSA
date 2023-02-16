import menuOperations as menuOP
import DataStructures.Queue.queueOP as queue

#Create menu obj
menuObj = menuOP.Menu()
queueObj = queue.Queue()

#Menu Options
menuObj.addMenuOp("Push to queue")
menuObj.addMenuOp("Pop queue")
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
            queueObj.enqueue(val)
    
        case 2:
            queueObj.dequeue()
        
        case 3:
            queueObj.display()
            
        case 4:
            menuObj.exitMenu()
    
        case _:
            print("\nInvalid Input!")
            pass
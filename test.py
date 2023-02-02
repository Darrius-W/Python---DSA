import menuOperations as menuOP
import Queue.queueOP as queue

#Create menu obj
menuObj = menuOP.Menu()
queueObj = queue.Queue()

#Menu Options
menuObj.addMenuOp("Enqueue")
menuObj.addMenuOp("Dequeue")
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
    
        case default:
            menuObj.exitMenu()
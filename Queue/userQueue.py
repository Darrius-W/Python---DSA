import queueOP

# Create Queue
userQueue = queueOP.Queue()
op = queueInput = None

print("New Queue has been created.")
# While loop
while op != 4:
    # Display user operations
    print("---------------------------\nSelect an Option:\n")
    print("1. Add to Queue.\n2. Remove from Queue.\n3. Display Queue\n4. Exit\n")
    print("Operation: ")
    
    # Request user operation input
    try:
        op = input()
    except:
        print("*** Error Invalid Input! ***\n")
        pass
    # Match user choice with selectecd operation and perform operation
    match op:
        # Enqueue
        case 1:
            queueInput = int(input("Enter value to input to Queue: "))
            queueOP.enqueue(queueInput)
            pass
        # Dequeue
        case 2:
            queueOP.dequeue()
            pass
        # Display Queue
        # Exit
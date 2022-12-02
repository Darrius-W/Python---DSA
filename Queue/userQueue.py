import queueOP

# Create Queue
userQueue = queueOP.Queue()
op = None

print("New Queue has been created.\n")
# While loop
while op is not 4:
    # Display user operations
    print("---------------------------\nSelect an Option:\n")
    print("1. Add to Queue.\n2. Remove from Queue.\n3. Display Queue\n4. Exit\n")
    print("Operation: ")
    
    # Request user operation input
    try:
        op = input(range(1,4))
    except:
        print("*** Error Invalid Input! ***\n")
        pass
    # Match user choice with selectecd operation and perform operation
        # Enqueue
        # Dequeue
        # Display Queue
        # Exit
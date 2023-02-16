# Linked List - Series of connected nodes where each node stores data & address of next node.
# Address of first node called HEAD, last node points to NULL.
# is a linear data structure.
'''
Example: a train, each train car is connected to one another
and each train car contains passengers aka data.
'''

# The structure of an individual node
class Node:
    def __init__(self, data):
        self.data = data #Data within a node
        self.next = None #Location of next node address
        

# The structure of a linked list        
class LinkedList:
    def __init__(self):
        self.head = None #Front node of linked list
        

# MAIN
if __name__ == '__main__':
    
    linkLst = LinkedList()
    
    # Assigning node data values
    linkLst.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    # Linking the nodes
    linkLst.head.next = second
    second.next = third
    
    # Printing the linked list
    while linkLst.head != None: #Until last node points to Null
        print(linkLst.head.data, end=" ")
        linkLst.head = linkLst.head.next #Traversing linked list to next node
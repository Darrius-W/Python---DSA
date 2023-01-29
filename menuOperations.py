'''
NEED TO ATTACH STRINGS TO THEIR FUNCTIONS
'''
'''
HANDLING MENU LIST

def hello():
    print('Hello\n')
    
def goodbye():
    print('Goodbye\n')

def display():
    menuStr = str()
    
    for item in lst:
        for val in item:
            if type(val) == int:
                menuStr = ("%d. " % val)
            else:
                menuStr+=val
        
        print(menuStr)
        del menuStr

lst =[
    [1, "Hello"],
    [2, "Goodbye"]
    ]
    
print(lst)    
display()
try:
    op = int(input('select option: '))
    if op < 1 or op > len(lst):
        raise opErr
    
except opErr:
    quit("ERROR: Invalid Entry\n")
    
i = 0
while i < len(lst):
    if op == lst[i][0]:
        print(lst[i][1])
        break
    i+=1
'''
class Menu:
    def __init__(self):
        self.funcCount = 0
        self.menu = list()
    
    def exitMenu(self):
            print("Goodbye!\n")
            exit(-1)
        
    def addMenuOp(self, str):
        #Remove Exit function if its the last func in list
        if self.funcCount >= 2:
            self.menu.pop()
            self.funcCount-=1
        
        
        #Add user func
        self.funcCount+=1
        self.menu.append(str)
        
        #Exit as the last func
        self.funcCount+=1
        self.menu.append("Exit")

   
    
    def displayMenu(self):
        '''if len(menu)  == 0:
            raise Exception("ERROR: No Options to Display\n")
            exit(-1)
        '''
            
        print("\nSelect an Option:\n---------------------------")
        index = 0
        for menuOp in self.menu:
            index+=1
            print("%d. %s" % (index, menuOp))


#Main
def add(x, y):
    sum = x + y
    return sum

#Create menu obj
menuObj = Menu()

'''
Add option to menu; args(string).
Menu obj should increase by 1 every time a Option gets added to menu.
Attach a function to an option
Adds exit option after first menu option added
'''
menuObj.addMenuOp("Add")
menuObj.addMenuOp("Add")
menuObj.addMenuOp("Add")
print(menuObj.funcCount)
menuObj.displayMenu()

#Ask user for input
userOp = int(input("Option: "))
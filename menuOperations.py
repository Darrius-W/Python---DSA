class Menu:
    def __init__(self):
        self.funcCount = 0
        self.menuLst = []
    
    def exitMenu(self):
            print("\nGoodbye!\n")
            exit(-1)
        
    def addMenuOp(self, str):
        #Remove Exit function if its the last func in list
        if self.funcCount >= 2:
            self.menuLst.pop()
            self.menuLst.pop()
            self.funcCount-=1
        
        #Add user func
        self.funcCount+=1
        self.menuLst+=(self.funcCount, str)
        
        #Exit as the last func
        self.funcCount+=1
        self.menuLst+=[self.funcCount, "Exit"]

   
    
    def displayMenu(self):
        print("\nSelect an Option:\n---------------------------")
        index = 0
        while index < len(self.menuLst):
            if index % 2 == 0:
                print("%i. %s" % (self.menuLst[index], self.menuLst[index+1]))
            index+=1
    
         
            
    def requestInput(self):
        userOp = int(input("\nOption: "))
        return userOp
import random
class train:
    def __init__(self, name, ID, next=None):
        self.name = name
        self.ID = random.randrange(100, 999)
        self.next = next
        
class linked:
    def __init__(self):
        self.head = None
        
    def insert(self, name, ID):
        car = train(name, ID)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = car
        else:
            self.head = car
            
    
    def printList(self):
        current = self.head
        while current:
            print("Type of train/car:", current.name, "ID:", current.ID)
            current = current.next
            
#----------------------------
cars = linked()
cars.insert("locomotive"," ")
cars.insert("coal"," ")
cars.insert("oil"," ")
cars.insert("auto"," ")
cars.insert("shipping"," ")
cars.printList()
#idk how to do the game loop portion

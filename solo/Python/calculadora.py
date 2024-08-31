class Calculadora:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y
    
    def minus(self):
        return self.x-self.y
    
    def multi(self):
        return self.x*self.y
    
    def division(self):
        return self.x/self.y
    
    def potentiation(self):
        return self.x**self.y
    
    
choice = 1

num = int(input("Choose a number: "))
num2 = int(input("Choose another number: "))
calc = Calculadora(num,num2)
while(choice != 0):
    choice = int(input("Enter your choice: \n"))
    print("0 to Exit")
    print("1 to add")
    print("2 to subtract")
    print("3 to multiplication")
    print("4 to division")
    print("5 to potentiation\n")
    
    if(choice == 0):
        break
    elif(choice == 1):
        print(f"Result: {calc.add()}\n")
    elif(choice == 2):
        print(f"Result: {calc.minus()}\n")
    elif(choice == 3):
        print(f"Result: {calc.multi()}\n")
    elif(choice == 4):
        print(f"Result: {calc.division()}\n")
    elif(choice == 5):
        print(f"Result: {calc.potentiation()}\n")
    else:
        print("Invalid Choice\n")
        

class Calculator:  # Class
    num = 100  # Class Variable

    def __init__(self, a, b):  # Constructor
        self.a = a  # Instance Variable
        self.b = b
        print("This is a Constructor Method in Calculator class")

    def data(self):  # Method
        print("This is a Data Method in Calculator Class")

    def Summation(self):
        return self.a + self.b + self.num


if __name__ == '__main__':
    obj = Calculator(1, 2)  # Create Object
    print(obj.Summation())

    obj1 = Calculator(2, 2)  # Create Another Object
    print(obj1.Summation())

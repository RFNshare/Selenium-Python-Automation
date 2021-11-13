from OOPdemo import Calculator


# Inheritance

class CalculatorChild(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def child_data(self):
        return self.Summation()


obj = CalculatorChild()
print(obj.child_data())

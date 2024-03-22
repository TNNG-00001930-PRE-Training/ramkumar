class Example:
    def __init__(self):
        pass

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

ex = Example()
ex.getString()
ex.printString()

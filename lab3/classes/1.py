class input_output:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input("Enrer: ")
    def printString(self):
        print(self.string.upper())

a = input_output()
a.getString()
a.printString()
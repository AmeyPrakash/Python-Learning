#Hiding the implementation details and showing only functionality to the user is called Abstraction.

class PC:
    def __init__(self):
        self.powerbutton = False
        self.screen = False

    def ON(self):
        self.powerbutton = True
        self.screen = True

        print("PC is ON")

p1 = PC()
p1.ON()
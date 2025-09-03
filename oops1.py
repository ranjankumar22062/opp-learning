#initiate a class
class student:
    #special medhod/magic method/dunder method -constructor
    def __init__(self):
        self.Roll="MEB22062"
        self.Department="Mechanical"
        self.year= "fourth"
    def travel(self, destination):
        print("This travel method was called manually")
        print (f"student now traveling to {destination}")
#create an obj/instance of the class
Ranjan=student()
Ranjan.travel("delhi")




        
#sample inhertance

## base class

class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} make a sound") 


## derived class
class Dog(Animal):

    def speak(self):
        print(f"{self.name} barks")   

animal=Animal("generic Animal")
animal.speak()

## create an instance of dog
dog=Dog("buddy")
dog.speak()

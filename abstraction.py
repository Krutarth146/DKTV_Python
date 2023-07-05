# Abstraction

# Shapes -----> circle, square, rectangle


from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self,color):
        self.color = color

    @abstractmethod
    def printsides(self):
        pass

    def printColor(self):           
        print(self.color)

class Triangle(Polygon):
    def __init__(self,color):
        super().__init__(color)

    def printsides(self):
        print("There are 3 Sides in Triangle")


# Abstract Methods have also concreate Methods
p = Triangle("Red")
p.printsides()
p.printColor()  # Red

# k = Polygon()
# k.printsides()  # TypeError: Can't instantiate abstract class Polygon with abstract method printsides
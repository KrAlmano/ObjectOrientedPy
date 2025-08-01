from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


    @abstractmethod
    def perimeter(self):
        pass

    def toString(self):
        print(self)



class Circle(Shape):
    
    PI = 3.14

    def __init__(self,radius):
        self.__radius = radius

    def area(self):
        area = self.PI*self.__radius**2
        print(area)

    def perimeter(self):
        perimeter = 2*self.PI*self.__radius
        print(perimeter)

    def toString(self):
        print("Circle radius = ",self.__radius)
    

class Square(Shape):
    def __init__(self,edge):
        self.__edge = edge

    def area(self):
        area= self.__edge**2
        print(area)

    def perimeter(self):
        perimeter= self.__edge*4
        print(perimeter)

    
    def toString(self):
        print("Square edge =",self.__edge)



c = Circle(5)
c.area()
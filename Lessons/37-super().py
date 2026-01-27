# super() = Function used in a child class to call methods from a parent class (superclass)
            # Allows to extend the functionality of the inherited methods

# class Circle:
#     def __init__(self, color, filled, radius):
#         self.color = color
#         self.filled = filled
#         self.radius = radius

# class Square:
#     def __init__(self, color, filled, width):
#         self.color = color
#         self.filled = filled
#         self.width = width

# class Triangle:
#     def __init__(self, color, filled, width, height):
#         self.color = color
#         self.filled = filled
#         self.width = width
#         self.height = height

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.141 * self.radius ** 2}cm²")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width ** 2}cm²")
    

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm²")

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

# print(triangle.color)
# print(triangle.is_filled)
# print(f"{triangle.width}cm")
# print(f"{triangle.height}cm")

# circle.describe()
# square.describe()
triangle.describe()


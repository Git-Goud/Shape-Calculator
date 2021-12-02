class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width**2) + (self.height**2))**.5

    #def get_picture(self):
    # return f"({self.set_width} * str("*"))\n ({self.set_height} * str("*"))\n"

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            #self.width or self.height > 50:
            return "Too big for picture."

        s = ""
        for row in range(self.height):
            s += "*" * self.width + "\n"
        return s

    def get_amount_inside(self, shape):
        shape_area = shape.height * shape.width
        original_area = self.get_area()
        return original_area // shape_area

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
  #The Python super() method lets you access methods from a parent class from within a child class. This helps reduce repetition in your code. One core feature of object-oriented programming languages like Python is inheritance. Inheritance is when a new class uses code from another class to create the new class.

  def __repr__(self):
   return f"Square(side={self.width})"
   
  def set_side(self, side):
   self.width = side
   self.height = side
   
  def set_width(self, side):
   self.set_side(side)
   
  def set_height(self, side):
   self.set_side(side)






























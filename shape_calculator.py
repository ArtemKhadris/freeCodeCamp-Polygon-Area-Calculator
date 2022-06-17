class Rectangle:

    # initialisation
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # size of rectangle (if we change it)
    def set_width(self, width):
        self.width = width
    def set_height (self, height):
        self.height = height

    # area of rectangle
    def get_area(self):
        return self.width * self.height

    # perimeter of rectangle
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # diagonal of rectangle
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # picture
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            a = ''
            for i in range(self.height):
                a += '*' * self.width + '\n'
            return a

    # how many rectangles we can put inside this rectangle
    def get_amount_inside(self, shape):
        a = self.width // shape.width
        b = self.height // shape.height
        return a * b

    # output
    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'
    
# square is a subclass of a rectangle
class Square(Rectangle):

    # initialisation
    def __init__(self, side):
        self.width = self.height = side

    # changing side of square
    def set_side(self, side):
        self.width = self.height = side

    # output
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
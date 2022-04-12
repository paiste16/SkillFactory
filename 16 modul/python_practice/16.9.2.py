class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def rectangle_width(self):
        return self.width

    def rectangle_heigth(self):
        return self.heigth

    def rectangle_area(self):
        return self.width * self.heigth

rect_1 = Rectangle(16,33)
print(rect_1.rectangle_width(),
      rect_1.rectangle_heigth(),
      rect_1.rectangle_area())
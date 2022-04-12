class Figures:
    def __init__(self, type, width, height, rad, cath_1, cath_2, hipoth, angle_a):
        self.height = height
        self.type = type
        self.width = width
        self.rad = rad
        self.cath_1 = cath_1
        self.cath_2 = cath_2
        self.hipoth = hipoth
        self.angle_a = angle_a

    def __str__(self):
        if self.type == "Rectangle":
            return f"{self.type} ({self.width}, {self.height})"
        elif self.type == "Circle":
            return f"{self.type} ({self.rad})"
        elif self.type == "Square":
            return f"{self.type} ({self.width})"
        elif self.type == "R_Triangle":
            return f"{self.type} ({self.cath_1}, {self.cath_2}, {self.hipoth}, {self.angle_a})"

Rect_1 = Figures("Rectangle", 56, 18, None, None, None, None, None)
print(Rect_1)
Circ_1 = Figures("Circle", None, None, 10, None, None, None, None)
print(Circ_1)
RTrian = Figures("R_Triangle", None, None, None, 3, 4, 5, 36.87)
print(RTrian)
Squar_1 = Figures("Square", 15, None, None, None, None, None, None)
print(Squar_1)



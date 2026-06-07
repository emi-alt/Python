class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        c_area = 3.14 * (self.radius)**2
        return c_area
    def perimeter(self):
        c_perimeter = 2 * 3.14 * self.radius
        return c_perimeter
user = int(input("Enter a radius to calculate the circle's area and perimeter: "))
circle = Circle(user)
print(f"The area of the circle is {circle.area()}.")
print(f"The perimeter of the circle is {circle.perimeter()}.")
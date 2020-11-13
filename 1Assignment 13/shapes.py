import matplotlib.pyplot as plt

class Shape:
  def __init__(self, base, height, color):
    self.base = base
    self.height = height
    self.color = color
  
  def describe(self):
    print("Base:", self.base)
    print("Height:", self.height)
    print("Color:", self.color)
    print("Perimeter:", self.perimeter)
    print("Area:", self.area)
    print("Vertices:", self.vertices)
  
  def render(self, filename):
    plt.clf()
    plt.style.use('bmh')
    plt.plot([x[0] for x in self.vertices]+[0], 
    [y[1] for y in self.vertices]+[0],
    color = self.color
    )
    plt.gca().set_aspect("equal")
    plt.savefig("1Assignment 13/filename.png")


class Rectangle(Shape):
  def __init__(self, base, height, color):
    super().__init__(base, height, color)
    self.perimeter = 2*base+2*height
    self.area = base*height
    self.vertices = [(0,0), (base,0), (base,height), (0,height)]


class RightTriangle(Shape):
  def __init__(self, base, height, color):
    super().__init__(base, height, color)
    self.perimeter = base+height+(base**2+height**2)**(1/2)
    self.area = (1/2)*base*height
    self.vertices = [(0,0), (base,0), (0,height)]


class Square(Rectangle):
  def __init__(self, base, color):
    super().__init__(base, base, color)


print('Testing Rectangle:')
rect = Rectangle(5,2,'red')
rect.describe()
rect.render('rectangle.png')
print('Rectangle done')

print('Testing Right Triangle:')
tri = RightTriangle(5,2,'blue')
tri.describe()
tri.render('rtriangle.png')
print('Right triangle done')

sq = Square(5,'green')
sq.describe()
sq.render('square.png')
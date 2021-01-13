class Student:

  def __init__(self, name, grade):
    self.name = name
    self.grade = grade
  
  def greeting(self):
    return "Hi I'm {} and I'm in grade {}".format(self.name, self.grade)
  

s = Student("Shelby", 6)

print(s.name)

print(s.grade)

print(s.greeting)

s = Student("Maurice", 8)

print(s.name)

print(s.grade)

print(s.greeting)
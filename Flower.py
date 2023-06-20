# Serhii Boiko, 20.06 
# Here we have class Flower and constructor method __init__ to initialize data: name, color. Then we create an object called p1 with passing arguments "Rose","red" , then we print name and color of object


class Flower: # Create a class; type: class, name Flower
  def __init__(self, name, color):  # constructor method __init__ to initialize data: name,color
    self.name = name # self shows that it is class attributes name and color
    self.color = color

p1 = Flower("Rose", "red") # here we create an object p1 of class Flowed where passing 2 arguments 
p2 = Flower("Peony","white") # here we create an object p2 of class Flowed where passing 2 arguments 

print(p1.name) # here we print name of object p1
print(p1.color) # here we print color of object p1
print(p2.name) # here we print name of object p2
print(p2.color) # here we print color of object p2

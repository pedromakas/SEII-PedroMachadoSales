class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show(self):
    print(f"I am {self.name} and I am {self.age} yo)
  
  def speak(self):
    print("I don't know what I say")
  
class Cat(Pet):
  def (self):
    print("Meow")
 
class Dog(Pet):
  def speak(self):
    print("Bark")
          
  @classmethod
  def number_of_people_(cls):
    return cls.number_of_people
          
  @classmethod
  def add_person(cls):
    cls.number_of_people += 1

class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
    
  def add_student(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    return False
  
  def get_average_grade(self):
    value = 0
    for student in self.students:
      value += student.get_grade()
    return value/len(self.students)
  
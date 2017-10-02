import random 
def main():
  students = [
    Student("Larsson,Halsted", 37),
    Student("BonJovi,Jon", 55),
    Student("Danvers,Lilly", 28)
  ]

  printHeader()
  selection = getUserSelection()

class Student:
  def __init__(self, lastName, firstname, age):
   self.lastName = lastName
   self.age = age
   self.firstName = firstname


  def assignRandomName(self):
      self.name = random.randint(0, 60)

  def assignRandomAge(self):
      self.age = random.randint(0, 100)

  def assignRandomWeight(self):
      self.wight = random.randint(80, 200)
      
  def assignRandomHeight(self):
      pass 

inputQuestions = [ 
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 3",
  "For SUM of STUDENT AGES type 4",
  "For AVERAGE of STUDENT AGES type 5",
]

def getUserSelection():
  (print) inputQuestion[0]
  (print) inputQuestion[1]
  (print) inputQuestion[2]
  return input("Type selection and press enter:")


def printHeader():
    print("HEADER TEXT HERE")

def printStudentsByAge():
  print "----Students By Age-----"

def printStudentsLName():
  print "----Students By -----"

def printStudentsFName():
  print "----Students By -----"

def printSumAge():
  print "Answer:"

def printAvgAge():
  print "Answer:"

def ageRange(studentA, studentB, studentC):
  pass


main()

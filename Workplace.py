
class Student:
  def __init__(Studentname, fname, lname):
    Studentname.firstname = fname
    Studentname.lastname = lname

  def printname(Studentname):
    print(Studentname.firstname, Studentname.lastname)
    
x = Student("Kevin", "Mbiyavanga")
x.printname()
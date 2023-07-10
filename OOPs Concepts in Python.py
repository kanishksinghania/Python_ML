class student:
  def __init__(self,name,rollno,m1,m2,m3,results):
    self.name=name
    self.rollno=rollno
    self.m1=m1
    self.m2=m2
    self.m3=m3
    self.results=results
  def getdata(self):
    self.name=input("Enter student name:")
    self.rollno=int(input("Enter roll number:"))
    self.m1=float(input("Marks1:"))
    self.m2=float(input("Marks2:"))
    self.m3=float(input("Marks3:"))
  def printdata(self):
    print("Student details are:")
    print("Name:",self.name)
    print("Roll number",self.rollno)
    print("Marks 1:",self.m1)
    print("Marks 2:",self.m2)
    print("Marks 3:",self.m3)
  def result(self):
    self.results=(self.m1+self.m2+self.m3)/3
    if (self.results>=40):
      print("Result is:",self.results,"%")
      print("Passed!!")
    else:
      print("Result is:",self.results,"%")
      print("Failed!!")

#main
#s1=student("",0,0.0,0.0,0.0,0)
n=int(input("Enter number of students:"))
for i in range(n):
  s1=student("",0,0.0,0.0,0.0,0)
  print("Student no: ",i)
  s1.getdata()
  s1.printdata()
  s1.result()

'''Enter number of students:2
Student no:  0
Enter student name:Kanishk Singhania
Enter roll number:15
Marks1:50
Marks2:60
Marks3:70
Student details are:
Name: Kanishk Singhania
Roll number 15
Marks 1: 50.0
Marks 2: 60.0
Marks 3: 70.0
Result is: 60.0 %
Passed!!
Student no:  1
Enter student name:Singhania
Enter roll number:1
Marks1:55
Marks2:65
Marks3:75
Student details are:
Name: Singhania
Roll number 1
Marks 1: 55.0
Marks 2: 65.0
Marks 3: 75.0
Result is: 65.0 %
Passed!!'''
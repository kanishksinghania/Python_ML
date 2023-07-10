#Write a python program that accepts the length of three sides of a triangle as inputs.
#The program should indicate whether or not the triangle is a right-angled triangle using function with exception handling.

#Let a,b,c be three sides of the triangle.
import sys
def largest(a,b,c):
    large=0
    if(a>b):
        if(a>c):
            large=a
        else:
            large=c
    else:
        if(b>c):
            large=b
        else:
            large=c
    return large
def right(s1,s2,h):
    p=((s1*s1)+(s2*s2))
    if (p==(h*h)):
        print("Triangle in right-angled triangle")
    else:
        print("triangle is not an right-angled triangle!")
#main
try:
  a=int(input("Enter side 1:"))
  b=int(input("Enter side 2:"))
  c=int(input("Enter side 3:"))
  d=largest(a,b,c)
  assert(a>0 and b>0 and c>0)
  if(d==a):
      right(b,c,a)
  elif(d==b):
      right(a,c,b)
  elif(d==c):
      right(a,b,c)
  print("Program done!!")
except:
  print("Error occured:",sys.exc_info()[0])


#exception handling assignment
import sys
l1=[5,0,6,'x',15]
for i in range(0,len(l1)):
  try:
    a=1/l1[i]
    print(a)
  except:
    print("Error occured:",sys.exc_info()[0])
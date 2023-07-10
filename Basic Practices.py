#exercise 1
from audioop import add

a = 9
b = 8
c = 7.56
d = 6.67
sum1 = a + b
sum2 = c + d
sub1 = a -b
sub2 = c - d
product1 = a*b
product2 = c*d
power1 = a**b
power2 = c**d
div1 = a/b
div2 = c/d
mod1 = a%b
mod2 = c%d
print(sum1)
print(sum2)
print(sub1)
print(sub2)
print(product1)
print(product2)
print(power1)
print(power2)
print(div1)
print(div2)
print(mod1)
print(mod2)
print(a>b)
print(a<b)
print(c>d)
print(c>d)
print(a>=b)
print(a<=b)
print(c>=d)
print(c>=d)


#exercise 2

name=input("Enter the name of student:\n")
rno=int(input("Enter the roll no. of student:\n"))
m1=int(input("Enter marks in subject 1 out of 100:\n"))
m2=int(input("Enter marks in subject 2 out of 100:\n"))
m3=int(input("Enter marks in subject 3 out of 100:\n"))
sum = m1 + m2 + m3
percentage = sum/3
print(name)
print(rno)
print("The percentage of marks is:",percentage)
if(m1>m2 and m1>m3):
   print("Subject 1 has highest marks")
elif(m2>m1 and m2>m3):
   print("Subject 2 has highest marks")
else:
    print("Subject 3 has highest marks")

if(m1<m2 and m1<m3):
    print("subject 1 has lowest marks")
elif(m2<m3 and m2<m3):
    print("Subject 2 has lowest marks")
else:
    print("Subject 3 has lowest marks") 


#exercise 3

num = int(input ("Enter any number to test whether it is odd or even:"))

if (num % 2) == 0:

              print ("The provided number is even")

else:

              print ("The provided number is odd") 


#exercise 4
num1 = int(input("Enter the value of 1st number:\n"))
num2 = int(input("Enter the value of 2nd number:\n"))
num3 = int(input("Enter the value of 3rd number:\n"))
num4 = int(input("Enter the value of 4th number:\n"))
num5 = int(input("Enter the value of 5th number:\n"))
print(num1**3)
print(num2**3)
print(num3**3)
print(num4**3)
print(num5**3)






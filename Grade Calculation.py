num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

#FAQ-Q2 Code
m1 = int(input("Enter the marks scored in mathematics out of 100:\n"))
if(m1>=90):
    print("The grade achieved is O")
elif(m1>=80 and m1<90):
    print("The grade achieved is A+")
elif(m1>=70 and m1<80):
    print("The grade achieved is A")
elif(m1>=60 and m1<70):
    print("The grade achieved is B+")
elif(m1>=50 and m1<60):
    print("The grade achieved is B")
elif(m1>=40 and m1<50):
    print("The grade achieved is P")
else:
    print("The grade acheived is F")                        
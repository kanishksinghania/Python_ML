#Q1
#1) Define a list called list_1 with four integer members, and find the output of the following
#2) Access the first three elements from list_1 using forward indices: list_1[0:3] 
#3) Access the last element from list_1 using the len function: list_1[len(list_1) - 1] 3) Access the last two elements from list_1 by slicing: list_1[-2:] 
#4) Access the first two elements using backward indices list_1[:-2] 
#5) Reverse the elements in the string: list_1[::-1]

list_1=[1,2,3,4]
print(list_1[0:3])
print(list_1[-1])
print(list_1[-2:])
print(list_1[:-2])
print(list_1[::-1])

#Q2 Accept 20 values from user and save it in list. Perform following operations on it 	
#a) count similar elements of list and print their index value   
#b) count even and odd values of list 
#c) count positive and negative values of list.

list_1=[]
for i in range(0,20):
  a=int(input("enter value:"))
  list_1.append(a)
print(list_1)
#(a)part
counter=[]
indexes=[]
l2=[]
for i in range(0,len(list_1)):
    if list_1[i] not in l2:
        l2.append(list_1[i])
for j in range(0,len(l2)):
    counter.append(list_1.count(l2[j]))
    l1=[]
    for k in range(0,len(list_1)):
        if list_1[k]==l2[j]:
            l1.append(k)
    indexes.append(l1)
for p in range(0,len(l2)):
    print("Element:",l2[p])
    print("Count:",counter[p])
    print("Indexes:",indexes[p])
#(b) part
l=len(list_1)
odd=[]
even=[]
for i in range(0,l):
  if (list_1[i])%2==0:
    even.append(list_1[i])
  else:
    odd.append(list_1[i])
print("even:",even)
print("odd",odd)
#(c)
pos=[]
neg=[]
for i in range(0,l):
  if list_1[i]>=0:
    pos.append(list_1[i])
  else:
    neg.append(list_1[i])
print("Positive values:",pos)
print("negative values:",neg)

#Q3 Accept 10 values from user and save it in list. Perform following operations on it  	
#a) Sort list in ascending order using sorted() function and display sorted list
#b) sort list in descending order using sort() function
#c) display length of list

list_1=[]
for i in range(10):
  a=int(input("enter value:"))
  list_1.append(a)
print("Original list:",list_1)
#(a)using sorted function for ascending order
print("(a)Using sorted function for ascending order")
print(sorted(list_1))
#(b)using sort function for descending order
print("(b)Using sort function for descending order")
list_1.sort(reverse=True)
print(list_1)
#(c)printing length of list
print("(c)Printing length of list")
print(len(list_1))

#Q4 Accept two lists from user and merge them using + in a single list.

list_1=[]
list_2=[]
print("For list 1")
for i in range(5):
  a=int(input("Enter value:"))
  list_1.append(a)
print("List 1:",list_1)
print("For list 2")
for i in range(5):
  b=int(input("Enter value:"))
  list_2.append(b)
print("List 2",list_2)
print("Performing merge function")
list_1=list_1+list_2
print("Merged list:",list_1)

#Q5 An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. 
# For example, RAM is an acronym for “random access memory.” 
# Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase. 
# Note: the acronym should be all uppercase, even if the words in the phrase are not capitalized.

l1=list(input("Enter phrase:").split(' '))
s1=''
for i in range(0,len(l1)):
  s1+=l1[i][0].upper()
print(s1)

#Q6 Write a program to print the abbreviation of a month, given its number.

months=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
a=int(input("Enter month number:"))
if a>12 or a<1:
  print("Invalid input!!")
else:
  print(months[a-1])




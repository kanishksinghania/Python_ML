#Q1 Assign 5 elements in the dictionary named my_dict. 
# This dictionary contains student’s information. Add and delete student information from my_dict.
#  Display student information

my_dict={'Name':'Kanishk','Rollno':15,'Panel':'E','Batch':'E1','Subject':'Python'}
print(my_dict)
#adding information
print("Adding information in dictionary")
my_dict['CGPA']=9.35
print(my_dict)
#deleting student information
print("Deleting information from dictionary")
del my_dict['CGPA']
print(my_dict)

#Q2	Convert list to dictionary
# e.g. list1=[‘name’, ‘panel’,’rollno’]
# list2=[‘ABC’,’B’,34]
# my_dict= { ‘name’:’ABC’, ‘panel’=’B’, ‘rollno’=34}

list1=['name','panel','rollno']
list2=['Kanishk','E',15]
dict_1={}
for i in range(0,len(list1)):
  dict_1[list1[i]]=list2[i]
print(dict_1)

#Q3	Sort the elements of the dictionary using sorted() function
# my_dict= { ‘name’:’ABC’, ‘panel’=’B’, ‘rollno’=34, ‘marks’:[65,87,67,94]}
# sorted(my_dict)

my_dict={'name': 'ABC', 'panel': 'B', 'rollno': 34,'marks':[65,8767,94]}
print(sorted(my_dict))

#Q4	Convert a dictionary to lists. Make one list of keys and other of values.

my_dict={'Name':'Kanishk','Rollno':15,'Panel':'E','Batch':'E1','Subject':'Python'}
l1=[]
l2=[]
for i in my_dict.keys():
  l1.append(i)
for j in my_dict.values():
  l2.append(j)
print("Keys list are:",l1)
print("Values list are:",l2)

#Q5	Find the mean of values of dictionary.
# e.g mydict= { ‘marks1’: 23, ‘marks2’: 123, ‘marks3’: 43, ‘marks4’: 13, ‘marks5’: 39)
# output: mean of all values.

my_dict={'marks1':23,'marks2':123,'marks3':43,'marks4':13,'marks5':39}
l1=[]
for i in my_dict.values():
  l1.append(i)
print("The mean of vales of dictionary is:",sum(l1)/len(l1))

#Q6	my_dict={‘name’:[‘Yash’,’Neel’,’Dev’], ‘rollno’:[11,12,13],’marks’:[78,56,98]}
#Perform following operations on above dictionary
#a)	Display name as Dev
#b)	Display 12 roll no
#c)	Display greatest marks

my_dict={'name':['yash','Neel','Dev'],'rollno':[11,12,13],'marks':[78,56,98]}
print("(a)part")
print(my_dict['name'][2])
print("(b)part")
print(my_dict['rollno'][1])
print("(c)part")
print(max(my_dict['marks']))

#Q7 Calculate frequency of letters occurring in a given string.

s1='abracadabra'
s2=''
for i in range(0,len(s1)):
  if s1[i] not in s2:
    s2+=s1[i]
dict_1={}
for j in range(0,len(s2)):
  dict_1[s2[j]]=s1.count(s2[j])
print(dict_1)

#Q8	Write a program which takes numerator and denominator values from the user 
# and gives output as a tuple of Quotient and Remainder.

n=int(input("enter numerator:"))
d=int(input("enter denominator:"))
q=n//d
r=n%d
tup1=(q,r)
print(tup1) 

#Q9	Suppose a date is represented as a tuple (d,m,y). 
# Write a program to create two date tuples with values taken from the user 
# and find the number of days between the two dates as an output.

print("Date 1")
d=int(input("Enter date:"))
m=int(input("enter month:"))
y=int(input("Enter year:"))
tup1=(d,m,y)
print("Date 2")
d2=int(input("Enter date:"))
m2=int(input("enter month:"))
y2=int(input("Enter year:"))
tup2=(d2,m2,y2)
a=abs(tup1[2]-tup2[2])*365
b=abs(tup1[1]-tup2[1])*30
c=abs(tup1[0]-tup2[0])
days=a+b+c
print(days)



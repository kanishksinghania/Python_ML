#numpy
import numpy as np
#array creation using existing python structures
#1.using list
myarr=np.array([[1,2,3]])
print(myarr[0])
print(myarr.shape)
print(myarr.dtype)
print(myarr.size)
#using dictionary
d=np.array({1,2,3})
print(d)
#using zeros
zeros=np.zeros((2,5))
print(zeros)
#using arange
rng=np.arange(5)
print(rng)
#using linspace
lin=np.linspace(1,50,5)
print(lin)
#using Iidentity
ide=np.identity(5)
print(ide)
arr=np.arange(10)
print(arr)
#reshape function
arr=arr.reshape(2,5)
print(arr)
#Ravel function
arr=arr.ravel()
print(arr)
#axis concept
#Axis=0 is for columns
#Axis=1 is for rows
x=[[1,2,3],[4,5,6],[7,8,9]]
arr1=np.array(x)
print(arr1.sum(axis=0))#print sum of each column
print(arr1.sum(axis=1))#print sum of each row
#transpose
#we use arr.T for transpose
arr2=arr1.T
print(arr2)
#creating an iterator
a=arr1.flat
for i in a:
    print(i)#this will print all elements of matrix
#operations
x1=[[1,0,1],[1,0,1],[1,0,1]]
arr2=np.array(x1)
x2=[[1,0,1],[1,0,1],[1,0,1]]
arr3=np.array(x2)
print(arr2+arr3)
print(arr2*arr3)
print(np.sqrt(arr2))
#to find specific element
s=np.where(arr2>0)#gives tuple of indices of elements greater than 0
print(s)
p=np.count_nonzero(arr2)#gives total number of non zero values in array
print(p)
i=np.nonzero(arr2)#gives tuple of array having indexes of non zer elements
print("NUmpy DONEEeee!!!")

'''[1 2 3]
(1, 3)
int64
3
{1, 2, 3}
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
[0 1 2 3 4]
[ 1.   13.25 25.5  37.75 50.  ]
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
[0 1 2 3 4 5 6 7 8 9]
[[0 1 2 3 4]
 [5 6 7 8 9]]
[0 1 2 3 4 5 6 7 8 9]
[12 15 18]
[ 6 15 24]
[[1 4 7]
 [2 5 8]
 [3 6 9]]
1
2
3
4
5
6
7
8
9
[[2 0 2]
 [2 0 2]
 [2 0 2]]
[[1 0 1]
 [1 0 1]
 [1 0 1]]
[[1. 0. 1.]
 [1. 0. 1.]
 [1. 0. 1.]]
(array([0, 0, 1, 1, 2, 2]), array([0, 2, 0, 2, 0, 2]))
6
NUmpy DONEEeee!!!'''
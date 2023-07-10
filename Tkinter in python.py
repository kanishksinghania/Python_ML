from tkinter import *
from datetime import datetime as d
def getval():
    a=d.today()
    ud=userdate.get()
    dt=ud.split('/')
    dt=d(int(dt[2]),int(dt[1]),int(dt[0]))
    diff=a-dt
    age=(diff.days)//365
    print("Your age is: ",age)
#main 
root=Tk()
root.geometry("644x344")
root.minsize(200,100)
root.maxsize(1200,988)
root.title("Python Assignment 11")
user=Label(root,text="Enter date:")
user.pack()
userdate=StringVar()
userentry=Entry(root,textvariable=userdate)
userentry.pack()
b1=Button(text="submit",command=getval)
b1.pack()
root.mainloop()

#Your age is: 18



# programm 1
# simple program to make root frame
# import tkinter
# root=tkinter.Tk()
# root.title("hello example")
# root.geometry("200x100")
# w=tkinter.Label(root,text="hello, world!")
# w.pack()
# root.mainloop()


# programm 2
# simple shorted program to make root frame
# from tkinter import *
# r=Tk()
# r.title("boss!!!")
# r.geometry("440x100")
# w=Label(r,text="hello sir utkarsh ")
# w.pack()
# r.mainloop()


# programm 3
# to make complicated program for "hello mouse world"
from tkinter import *
root=Tk()
root.title("hello mouse world")
root.geometry("400x400")
canvas=Canvas(root)

def sayhello():
    global text
    text="hello"
    print("hello")

def saygoodbye():
    global text
    text="goodbye"
    print("goodbye")

def buttonpressed(evt):
    if evt.widget == canvas:
        canvas.create_text(evt.x,evt.y,text=text)

hellob=Button(root,text="hello",command=saygoodbye)

goodbyeb=Button(root,text="good bye",command=saygoodbye)

root.bind("Button-1",buttonpressed)

canvas.pack()
hellob.pack()
goodbyeb.pack()

root.mainloop()


"""
l=10  #global
def fun():
    l=12  #local
    print(l)
fun()
print(l)

output:
12
10
"""

"""
def fun():
   x=20
   def fun1():
        global x
        x=88
   print("before calling fun1",x)
   fun1()
   print("after calling fun",x)
fun()
print(x)
"""


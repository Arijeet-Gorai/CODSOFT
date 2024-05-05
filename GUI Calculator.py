from tkinter import *
class calculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x450")
        self.root.minsize(500,250)
        self.root.maxsize(700,350)
        self.root.title("A Simple Calculator")
        self.root.configure(bg='pink')
        self.root.iconbitmap(r'D:\Python\CODSOFT\icon1.ico')


        Label(self.root,text="First Number",font=('verdana',20),bg='pink',fg='black').grid(row=0,column=0)
        self.text1=Entry(self.root,font=('arial',15))
        self.text1.grid(row=0,column=1)

        Label(self.root,text="Second Number",font=('verdana',20),bg='pink',fg='black').grid(row=1,column=0)
        self.text2=Entry(self.root,font=('arial',15))
        self.text2.grid(row=1,column=1)

        Label(self.root,text="Result",font=('verdana',20),bg='pink',fg='black').grid(row=2,column=0)
        self.text3=Entry(self.root,font=('arial',15))
        self.text3.grid(row=2,column=1)

        self.button1=Button(self.root,text='+',font=("verdana",20),bg='blue',fg='red',command=self.sum)
        self.button1.grid(row=3,column=0,sticky='e')

        self.button2=Button(self.root,text='-',font=("verdana",20),bg='blue',fg='red',command=self.sub)
        self.button2.grid(row=3,column=1,sticky='w')

        self.button3=Button(self.root,text='x',font=("verdana",20),bg='blue',fg='red',command=self.mul)
        self.button3.grid(row=4,column=0,sticky='e')

        self.button4=Button(self.root,text='/',font=("verdana",20),bg='blue',fg='red',command=self.div)
        self.button4.grid(row=4,column=1,sticky='w')
        self.root.mainloop()


    def sum (self):
        a=self.text1.get()
        b=self.text2.get()
        c=int(a)+int(b)
        self.text3.delete(0,END)
        self.text3.insert(0,c)
    def sub (self):
        a=self.text1.get()
        b=self.text2.get()
        c=int(a)-int(b)
        self.text3.delete(0,END)
        self.text3.insert(0,c)
    def mul (self):
        a=self.text1.get()
        b=self.text2.get()
        c=int(a)*int(b)
        self.text3.delete(0,END)
        self.text3.insert(0,c)
    def div (self):
        a=self.text1.get()
        b=self.text2.get()
        c=int(a)/int(b)
        self.text3.delete(0,END)
        self.text3.insert(0,c)

obj=calculator()

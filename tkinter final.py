from tkinter import *
mw=Tk()
def call():
    res=int(e1.get())*c1+int(e2.get())*c2+int(e3.get())*c3+int(e4.get())*c4+int(e5.get())*c5+int(e6.get())*c6
    service=res/100
    service=service*15

    sal=res/100
    sal*=5
    
    cost.set(res)#cost
    servicetax.set(service)#service
    saltax.set(sal)#sal tax
    subtotal.set(sal+service)#subtotal
    t.set(res+sal+service)#subtotal



def reset():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)
    e13.delete(0,END)


cost=StringVar()
t=StringVar()
servicetax=StringVar()
saltax=StringVar()
subtotal=StringVar()


l1=Label(mw,text="Flavours rsetaruant",font="18") # snack menu
l2=Label(mw,text="Fries",font="18") # snack menu
l3=Label(mw,text="Noodels",font="18") # snack menu
l4=Label(mw,text="Soup",font="18") # snack menu
l5=Label(mw,text="Burger",font="18") # snack menu
l6=Label(mw,text="Sandwich",font="18") # snack menu
l7=Label(mw,text="Drinks",font="18") # snack menu


l14=Label(mw,text="30/-",font="18") # snack menu
l15=Label(mw,text="30/-",font="18") # snack menu
l16=Label(mw,text="10/-",font="18") # snack menu
l17=Label(mw,text="25/-",font="18") # snack menu
l18=Label(mw,text="35/-",font="18") # snack menu
l19=Label(mw,text="10/-",font="18") # snack menu



l10=Label(mw,text="Cost",font="18") # snack menu
l11=Label(mw,text="Service charge",font="18") # snack menu
l12=Label(mw,text="sales tax",font="18") # snack menu
l13=Label(mw,text="Subtotal",font="18") # snack menu
Total=Label(mw,text="Total",font="18")



e1=Entry(mw)#entry box 1
e2=Entry(mw)#entry box 2
e3=Entry(mw)#entry box 3
e4=Entry(mw)#entry box 4
e5=Entry(mw)#entry box 5
e6=Entry(mw)#entry box 6

e9=Entry(mw,textvariable=cost)#displays cost
e10=Entry(mw,textvariable=servicetax)#displays Service charge 15%
e11=Entry(mw,textvariable=saltax)#displays sales tax 5%
e12=Entry(mw,textvariable=subtotal)#sub total
e13=Entry(mw,textvariable=t)#displays total amount

b1=Button(mw,text="Total",font="18",command=call)#for cost,tax,total amount
b2=Button(mw,text="Reset",font="18",command=reset)#set all entry boxes empty
b3=Button(mw,text="pay",font="18")# no action only just button


c1,c2,c3,c4,c5,c6=30,30,10,25,35,10


l1.place(x=690,y=0)  #snack menu placed
l2.place(x=10,y=100)  #snack menu placed
l3.place(x=10,y=150) #snack menu placed
l4.place(x=10,y=200) #snack menu placed
l5.place(x=10,y=250) #snack menu placed
l6.place(x=10,y=300)  #snack menu placed
l7.place(x=10,y=350)  #snack menu placed

l14.place(x=295,y=100) #snack menu placed
l15.place(x=295,y=155) #snack menu placed
l16.place(x=295,y=205) #snack menu placed
l17.place(x=295,y=255) #snack menu placed
l18.place(x=295,y=305) #snack menu placed
l19.place(x=295,y=355) #snack menu placed


l10.place(x=520,y=100)  #snack menu placed
l11.place(x=440,y=150)  #snack menu placed
l12.place(x=490,y=200)  #snack menu placed
l13.place(x=490,y=250)  #snack menu placed
Total.place(x=520,y=300)








e1.place(x=120,y=105)#entry box placed
e2.place(x=120,y=155)#entry box placed
e3.place(x=120,y=205)#entry box placed
e4.place(x=120,y=255)#entry box placed
e5.place(x=120,y=305)#entry box placed
e6.place(x=120,y=355)#entry box placed


e9.place(x=600,y=105)#entry box placed
e10.place(x=600,y=155)#entry box placed
e11.place(x=600,y=205)#entry box placed
e12.place(x=600,y=255)#entry box placed
e13.place(x=600,y=305)#entry box placed

b1.place(x=10,y=455) #button 1
b2.place(x=100,y=455) #button 1
b3.place(x=200,y=455) #button 1



mw.mainloop()

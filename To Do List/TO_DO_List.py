from tkinter import *

app=Tk()
app.title("To-Do List")
app.geometry("400x650+400+100")
app.resizable(False,False)

tasks=[]

def addtsk():
    tsk=tsk_entry.get()
    tsk_entry.delete(0,END)
    if tsk:
        with open("tasklist.txt",'a') as file:
            file.write(f"\n{tsk}")
        tasks.append(tsk)
        list.insert(END,tsk)

def dlttsk():
    global tasks
    tsk=str(list.get(ANCHOR))
    if tsk in tasks:
        tasks.remove(tsk)
        with open("tasklist.txt",'w') as fl:
            for tsk in tasks:
                fl.write(tsk+"\n")
        list.delete(ANCHOR)
        
def opntask():
    try:
        global tasks
        with open("tasllist.txt","r")as f:
            task=f.readline()
        for t in task:
            if t!="\n":
                tasks.append(t)
                list.insert(END,t)
    except:
        file=open('tasklist.txt','w')
        file.close()

img=PhotoImage(file="D:\\Codsoft\\To Do List\\Images\\task.png")
app.iconphoto(False,img)

top=PhotoImage(file="D:\\Codsoft\\To Do List\\Images\\topbar.png")
Label(app,image=top).pack()

nte=PhotoImage(file="D:\\Codsoft\\To Do List\\Images\\task.png")
Label(app,image=nte,bg='#32405b').place(x=30,y=25)

head=Label(app,text="ALL TASK",font="arial 20 bold",fg="white",bg='#32405b')
head.place(x=130,y=25)

frame=Frame(app,width=400,height=50,bg="white")
frame.place(x=0,y=180)

tsk=StringVar()
tsk_entry=Entry(frame,width=18,font="arial 20",bd=0)
tsk_entry.place(x=10,y=7)
tsk_entry.focus()

bttn=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addtsk).place(x=300,y=0)

frame1=Frame(app,bd=3,width=700,height=200,bg="#32405b")
frame1.pack(pady=(160,0))

list=Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",selectbackground="#5a95ff")
list.pack(side=LEFT,fill=BOTH,padx=2)
scroll=Scrollbar(frame1)
scroll.pack(side=RIGHT,fill=BOTH)

list.config(yscrollcommand=scroll.set)
scroll.config(command=list.yview)

dlt=PhotoImage(file="D:\\Codsoft\\To Do List\\Images\\delete.png")
Button(app,image=dlt,bd=0,command=dlttsk).pack(side=BOTTOM,pady=13)

app.mainloop()
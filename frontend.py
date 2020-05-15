from tkinter import *
import backend

def get_selected_row(event):
    global selected_row
    index = list_box.curselection()[0]
    selected_row = list_box.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def delete_command():
    backend.delete(selected_row[0])

def view_command():
    list_box.delete(0,END)
    for row in backend.view():
        list_box.insert(END,row)

def search_command():
    list_box.delete(0,END)
    for row in backend.search(date_text.get(),Programming_text.get(),Reading_text.get(),Exercise_text.get(),Studying_text.get(),Earnings_text.get()):
        list_box.insert(END,row)

def add_command():
    backend.insert(date_text.get(),Programming_text.get(),Reading_text.get(),Exercise_text.get(),Studying_text.get(),Earnings_text.get())

    list_box.delete(0,END)
    list_box.insert(END,(date_text.get(),Programming_text.get(),Reading_text.get(),Exercise_text.get(),Studying_text.get(),Earnings_text.get()))

win = Tk()

win.wm_title('MY ROUTINE DATABASE')


l1 = Label(win,text = "Date")
l1.grid(column =0, row = 0)

l2 = Label(win,text = "Programming")
l2.grid(column =2, row = 0)

l3 = Label(win,text = "Reading")
l3.grid(column =0, row = 1)

l4 = Label(win,text = "Exercise")
l4.grid(column =2, row = 1)

l5 = Label(win,text = "Studying")
l5.grid(column =0, row = 2)

l6 = Label(win,text = "Earnings")
l6.grid(column =2, row = 2)


date_text = StringVar()
e1 = Entry(win,textvariable=date_text)
e1.grid(column=1,row=0)

Programming_text = StringVar()
e2 = Entry(win,textvariable=Programming_text)
e2.grid(column=3,row=0)

Reading_text = StringVar()
e3 = Entry(win,textvariable=Reading_text)
e3.grid(column=1,row=1)

Exercise_text = StringVar()
e4 = Entry(win,textvariable=Exercise_text)
e4.grid(column=3,row=1)

Studying_text = StringVar()
e5 = Entry(win,textvariable=Studying_text)
e5.grid(column=1,row=2)

Earnings_text = StringVar()
e6 = Entry(win,textvariable=Earnings_text)
e6.grid(column=3,row=2)


list_box = Listbox(win,height=8,width=35)
list_box.grid(row=3,column=0,rowspan=9,columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3,column=2,rowspan=9)

list_box.bind('<<ListboxSelect>>',get_selected_row)


b1 = Button(win,text='ADD',width=12,pady=5,command=add_command)
b1.grid(row=3,column=3)

b2 = Button(win,text='Search',width=12,pady=5,command=search_command)
b2.grid(row=4,column=3)

b3 = Button(win,text='Delete date',width=12,pady=5,command=delete_command)
b3.grid(row=5,column=3)

b4 = Button(win,text='View all',width=12,pady=5,command=view_command)
b4.grid(row=6,column=3)

b5 = Button(win,text='Close',width=12,pady=5,command = win.destroy)
b5.grid(row=7,column=3)


win.mainloop()

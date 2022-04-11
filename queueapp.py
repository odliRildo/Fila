from tkinter import *
from tkinter import messagebox
from sqlitequeue import Database
from time import asctime
db = Database('Monitoria.db')

def populate_list():
    Fila.delete(0,END)
    for row in db.fetch():
        Fila.insert(END, row)

def add_item():
    if part_text.get() == '':
        messagebox.showerror('Não Preenchido','Preencha o(s) campos!')
        return
    db.insert(part_text.get(), asctime())
    Fila.delete(0,END)
    Fila.insert(END, (part_text.get(), asctime()))
    populate_list()

def select_item(event):
    global selected_item
    index = Fila.curselection()[0]
    selected_item = Fila.get(index)
    
    pessoa_entry.delete(0,END)
    pessoa_entry.insert(END, selected_item[1])

def remove_item():
    db.remove(selected_item[0])
    populate_list()

#Create Window Object
app = Tk()



#Part
part_text = StringVar()
pessoa = Label(app, text = 'Nome', font=("bold",15), pady=20)
pessoa.grid(row=0,column=0)
pessoa_entry = Entry(app,textvariable=part_text,border=0, justify='left',)
pessoa_entry.grid(row=0, column = 1)

#Fila
Fila = Listbox(app,height=30,width=50,border=0)
Fila.grid(row=2, column=0, columnspan=3, rowspan=6, pady= 20, padx= 20)


#scroll
scrollbar = Scrollbar(app)
scrollbar.grid(row=2,column=2,sticky=E)

#set scroll to queue
Fila.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=Fila.yview)

#Buttons
add_btn = Button(app, text='Adicionar',width=12,command=add_item)
add_btn.grid(row=1,column=0,pady=20)
remove_btn = Button(app, text='Remover',width=12,command=remove_item)
remove_btn.grid(row=1,column=1,pady=20)

#Bind Select
Fila.bind('<<ListboxSelect>>',select_item)


app.title('Fila Monitoria')
app.geometry('350x700')
populate_list()
#Start Program
app.mainloop()
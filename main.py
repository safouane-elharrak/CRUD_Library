from tkinter import *
from tkinter import ttk
import lxml.etree
#importing the xml file 
import xml.etree.ElementTree as ET

root = Tk()
root.title("Library")
root.geometry("620x600")
root.configure(bg='snow')


#CRUD Functions
#Add
def addBook():
    mytree= ET.parse('library.xml')
    myroot= mytree.getroot()

    nums = list()
    if not myroot.findall('book'):
        nums.append(1)
    else:
        for book in myroot.findall('book'):
            nums.append(book.get('num'))
    
    nextNum= int(nums[-1]) + 1
    newNum = ET.SubElement(myroot,"book", num=str(nextNum) , type= cmb.get())
    ET.SubElement(newNum, "title", name="title").text = widgetTitle.get()
    ET.SubElement(newNum, "author", name="author").text = widgetAuthor.get()
    mytree.write("library.xml")

    cmb.current(0)
    widgetAuthor.delete(0,END)
    widgetTitle.delete(0,END)
    read()

#Read
def read(): 
    mytree= ET.parse('library.xml')
    myroot= mytree.getroot() 
    #clean rows
    for row in my_tree.get_children():
        my_tree.delete(row)
    #insert
    for book in myroot.findall('book'):
        my_tree.insert(parent='', index='end', iid=int(book.get('num')), text="", values=(book.get('num'),book.find('title').text, book.find('author').text,book.get('type')), tag ="orow")

#Delete
def delete():
    mytree = ET.parse('library.xml')
    myroot = mytree.getroot()

    for book in myroot.findall('book'):
        nums=book.get('num')
        num = int(my_tree.focus())
        for siid in nums:
            if int(siid) == num:
                myroot.remove(book)
                mytree.write("library.xml")
    read()
        
#Update
def update():
    mytree = ET.parse('library.xml')
    myroot = mytree.getroot()
    num = int(my_tree.focus())+1

    for book in myroot.findall('book'):
        if int(book.get('num'))== num:
            book.set('type', widgetType.get())
            book.find('author').text= widgetAuthor.get()
            book.find('title').text= widgetTitle.get()
            mytree.write("library.xml")
    editor.destroy()
    root.deiconify()
    read()
#Edit
def edit():
    root.withdraw()
    global editor
    editor = Tk()
    editor.title('Update')
    editor.geometry("300x150")

    #Test box names 
    global type_editor
    global title_editor
    global author_editor

    type = ["Fiction", "Drame","Aventure","Policier"]
    #text Boxes 
    type_editor= ttk.Combobox(editor, values=type)
    type_editor.grid(row=0, column=1, padx=20, pady=(10,0))
    type_editor.current(0) 
    title_editor = Entry(editor, width=30)
    title_editor.grid(row=1, column=1)
    author_editor = Entry(editor, width=30)
    author_editor.grid(row=2, column=1)

    #Text Box labels 
    typeLabel= Label(editor , text="Type")
    typeLabel.grid(row=0, column=0 , pady=(10,0))
    titleLabel= Label(editor , text="Title")
    titleLabel.grid(row=1, column=0)
    authorLabel= Label(editor , text="Author")
    authorLabel.grid(row=2, column=0)

    mytree = ET.parse('library.xml')
    myroot = mytree.getroot()

    num = int(my_tree.focus())+1
    for book in myroot.findall('book'):
        if int(book.get('num'))== num:
            for idx, type in enumerate(type):
                if type == book.get('type'):
                    type_editor.current(idx)
                title_editor.insert(0, book.find('title').text)
                author_editor.insert(0,book.find('author').text)
    
    edit_btn = Button(
    editor, text="Edit", padx=3, pady=3, width=3,
    bd=3, font=('Arial', 10), bg="dodger blue", command=update)
    edit_btn.grid(row=6, column=1)


#interface
my_tree = ttk.Treeview(root)
libraryName = "Library"

titleL = Label(root, text=libraryName, font=('Helvetica', 30, 'bold'), fg="blue4", bd=2, bg='snow')
titleL.grid(row=0, column=0, columnspan=4, padx=250, pady=20)

numeroLabel = Label(root, text="Number", font=('Helvetica', 18),fg="blue4", bg='snow')
titleLabel = Label(root, text="Title", font=('Helvetica', 18),fg="blue4", bg='snow')
authorLabel = Label(root, text="Author", font=('Helvetica', 18),fg="blue4", bg='snow')
typeLabel = Label(root, text="Type", font=('Helvetica', 18),fg="blue4", bg='snow')

numeroLabel.grid(row=1, column=0, padx=10, pady=10)
titleLabel.grid(row=2, column=0, padx=10, pady=10)
authorLabel.grid(row=3, column=0, padx=10, pady=10)
typeLabel.grid(row=4, column=0, padx=10, pady=10)
type = ["Fiction", "Drame","Aventure","Policier"]

#entry() => The Entry widget is used to accept single-line text strings from a user
widgetNumero = Entry(root, width=25, bd=5, font=('Arial bold', 18))
widgetTitle = Entry(root, width=25, bd=5, font=('Arial bold', 18))
widgetAuthor = Entry(root, width=25, bd=5, font=('Arial bold', 18))
widgetType = Entry(root, width=25, bd=5, font=('Arial bold', 18))
#grid()  => geometry manager organizes widgets in a table-like structure in the parent widget=>widget.grid( grid_options )
widgetNumero.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
widgetTitle.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
widgetAuthor.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
#combo box -type 
cmb=ttk.Combobox(root,value=type, width=33, font=('Arial', 15))
cmb.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
cmb.current(1)

#Buttons
addBtn = Button(
    root, text="Add", padx=5, pady=5, width=5,
    bd=3, font=('Arial bold', 15), bg="light blue",command=addBook, fg="green") 
addBtn.grid(row=7, column=0)

updateBtn = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Arial bold', 15), bg="light blue", command=edit, fg="blue4")
updateBtn.grid(row=7, column=1)

deleteBtn = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial bold', 15), bg="light blue" , command=delete, fg="red4")
deleteBtn.grid(row=7, column=2)


style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))


#liste des livres 
my_tree['columns'] = ("num", "title", "author", "type")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("num", anchor=W, width=70)
my_tree.column("title", anchor=W, width=200)
my_tree.column("author", anchor=W, width=200)
my_tree.column("type", anchor=W, width=100)

my_tree.heading("num", text="NUM", anchor=W)
my_tree.heading("title", text="Title", anchor=W)
my_tree.heading("author", text="Author", anchor=W)
my_tree.heading("type", text="Type", anchor=W)

my_tree.tag_configure('orow', background='LightSkyBlue1', font=('Arial bold', 15))
my_tree.grid(row=10, column=0, columnspan=4, rowspan=5, padx=10, pady=10)


    
read()
root.mainloop()
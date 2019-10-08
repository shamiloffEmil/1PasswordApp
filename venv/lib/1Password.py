# -*- coding: utf-8 -*

import json
import os
import tkinter
from tkinter import *
from zipfile import *


class FirstPage:

    def __init__(self):
        self.mainWindow()

    def mainWindow(self):
        fileJSON = "data_file.json"
        fileZIP = "data_file.zip"

        root2 = Tk()
        root2.geometry('300x300')
        root2.title('1Password')

        def new_window():
            root2.destroy()
            self.listWindow()

        def checkArchive(fzip):

            if not os.path.isfile(fzip):
                return False
            else:
                return True

        def checkPassword(self):
            z = ZipFile('data_file.zip', 'r')

            try:
                z.extract('data_file.json',None,val.get().encode('cp850','replace'))
                new_window()
            except RuntimeError:
                entry.delete(0,END)
                print('Invalid password')





        val = StringVar()

        if checkArchive(fileZIP):
            lab = Label(root2, text='Авторизация')
            but = Button(root2, text='Ok')
            but.bind('<Button->', checkPassword)
            entry = Entry(root2, textvariable=val,show="*")

            lab.pack()
            but.pack()
            entry.pack()
            root2.mainloop()

        else:
            new_window()



    def listWindow(self):
        self.root = Tk()
        self.l = Listbox(selectmode=EXTENDED)
        self.l.pack(side=TOP)
        self.b = Button(text="Посмотреть", command=self.showPassword)
        self.b.pack()
        self.label1 = Label(text="")
        self.label2 = Label(text="")
        self.label1.pack()
        self.label2.pack()
        self.data = {}
        self.FillInList()
        self.root.mainloop()

    def unpacking(self):
        with open("data_file.json", "r") as read_file:
            loadData = json.load(read_file)[0]
            self.data = loadData

    def FillInList(self):
        self.unpacking()
        for key in self.data:
            self.l.insert(END, key)#self.data[key])

    def showPassword(self):
        selecion = self.l.curselection()
        key = self.l.get(selecion[0])
        JString = self.data.get(key)
        self.label1['text'] = JString.get('login')
        self.label2['text'] = JString.get('password')

if __name__ == '__main__':
    FirstPage()

'''
def addItem():
    lbox.insert(END, entry.get())
    entry.delete(0, END)


def delList():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)


def saveList():
    f = open('list000.txt', 'w')
    f.writelines("\n".join(lbox.get(0, END)))
    f.close()


root = Tk()

lbox = Listbox(selectmode=EXTENDED)
lbox.pack(side=LEFT)
scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)
lbox.config(yscrollcommand=scroll.set)

f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)
entry.pack(anchor=N)
badd = Button(f, text="Add", command=addItem)
badd.pack(fill=X)
bdel = Button(f, text="Delete", command=delList)
bdel.pack(fill=X)
bsave = Button(f, text="Save", command=saveList)
bsave.pack(fill=X)

root.mainloop()
'''

'''
class Block:
    def __init__(self, master):
        self.e = Entry(master, width=20)
        self.b = Button(master, text="Преобразовать")
        self.l = Label(master, bg='black', fg='white', width=20)
        self.e.pack()
        self.b.pack()
        self.l.pack()

    def setFunc(self, func):
        self.b['command'] = eval('self.' + func)

    def strToSortlist(self):
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l['text'] = ' '.join(s)

    def strReverse(self):
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l['text'] = ' '.join(s)


root = Tk()

first_block = Block(root)
first_block.setFunc('strToSortlist')

second_block = Block(root)
second_block.setFunc('strReverse')

root.mainloop()
'''
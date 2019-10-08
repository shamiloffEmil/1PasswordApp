# -*- coding: utf-8 -*

import json
import os

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from zipfile import *


class Page(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Page1)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
            #print(frame_class)
            print(self._frame)

        self._frame = new_frame
        self._frame.pack()


class Page1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.val = StringVar()
        self.master = master
        self.message = Label(self, text='Invalid password')


        fileZIP = "data_file.zip"  # type: str

        def checkPassword(event):

            z = ZipFile('data_file.zip', 'r')
            pas = self.val.get().encode('cp850', 'replace')
            try:
                z.extract('data_file.json', None, pas)
                z.close()
                self.master.switch_frame(Page2)

            except RuntimeError:
                tk.entry.delete(0, END)
                self.message.pack()

        def checkArchive(fzip):

            if not os.path.isfile(fzip):
                return False
            else:
                return True

        if checkArchive(fileZIP):
            tk.lab = Label(self, text='Авторизация')
            tk.butOK = Button(self, text='Ok')
            tk.butOK.bind('<Button->', checkPassword)
            tk.entry = Entry(self, textvariable=self.val, show="*")

            tk.lab.pack()
            tk.butOK.pack()
            tk.entry.pack()

        else:

            self.master.switch_frame(Page2)


class Page2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        tk.master = master
        tk.l = Listbox(selectmode=EXTENDED)
        tk.l.bind('<<ListboxSelect>>', self.onselect)
        tk.l.pack(side=TOP)
        tk.site = ''
        tk.login = ''
        tk.password = ''
        self.data = {}
        self.FillInList()
        tk.entryLogin = Entry(self, textvariable="")
        tk.entryPassword = Entry(self, textvariable="")
        tk.entryLogin.pack()
        tk.entryPassword.pack()
        tk.bPlus = Button(text="+", command=self.newSite)
        tk.bMinus = Button(text="-", command=self.deleteSite)
        tk.btun = Button(text="Изменить", command=self.addSite)
        tk.btun.pack()
        tk.bPlus.pack()
        tk.bMinus.pack()
        self.entrySite = Entry(self, textvariable="")
        self.entrySite.pack_forget()
        self.counterButtonSave = 0
        # tk.Button(self, text="Return to start page",
        #          command=lambda: master.switch_frame(Page1)).pack()
        #self.master.switch_frame(Page3)

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def showPassword(self):

       selecion = tk.l.curselection()
       key = tk.l.get(selecion[0])
       JString = self.data.get(key)
       self.site = key
       tk.login = JString.get('login')
       tk.password = JString.get('password')

       tk.entryLogin.delete(0, END)
       tk.entryPassword.delete(0, END)
       self.entrySite.delete(0, END)
       tk.entryLogin.insert(0, tk.login)
       tk.entryPassword.insert(0, tk.password)
       self.entrySite.insert(0,self.site)

        #tk.master.switch_frame(Page3)  не убивает текущую страницу??????

    def onselect(self,a):
        selecion = tk.l.curselection()
        key = tk.l.get(selecion[0])
        JString = self.data.get(key)

        self.site = key
        tk.login = JString.get('login')
        tk.password = JString.get('password')

        tk.entryLogin.delete(0, END)
        tk.entryPassword.delete(0, END)
        self.entrySite.delete(0, END)
        tk.entryLogin.insert(0, tk.login)
        tk.entryPassword.insert(0, tk.password)
        self.entrySite.insert(0, self.site)


    def deleteSite(self):
        selection = tk.l.curselection()
        tk.l.delete(selection[0])

    def addSite(self):
        #self.entrySite = Entry(self, textvariable="")
        #self.entrySite.pack()
        #self.entrySite.insert(0, self.site)
        self.counterButtonSave+=1;

        if self.counterButtonSave ==1:
            self.entrySite.pack()
            tk.bAdd = Button(text="Сохранить", command=self.saveInLabel).pack()

        tk.btun.pack_forget()

    def newSite(self):
        self.counterButtonSave += 1;
        self.site = ''

        if self.counterButtonSave == 1:
            self.entrySite.pack()
            tk.bAdd = Button(text="Сохранить", command=self.saveInLabel).pack()


        self.entrySite.delete(0, END)
        tk.entryLogin.delete(0, END)
        tk.entryPassword.delete(0, END)


    def saveInLabel(self):
        if self.site == self.entrySite.get():
            ourDictionary = self.data[self.site]
            ourDictionary.update({
            'login':''+tk.entryLogin.get()+'','password':''+tk.entryPassword.get()+''
            })
        elif self.site  == '':
            self.data[self.entrySite.get()] = {'login': '' + tk.entryLogin.get() + '', 'password': '' + tk.entryPassword.get() + ''}
        else:
            self.data[self.entrySite.get()] = self.data.pop(self.site)
            self.site = self.entrySite.get()

            ourDictionary = self.data[self.site]
            ourDictionary.update({
            'login': '' + tk.entryLogin.get() + '', 'password': '' + tk.entryPassword.get() + ''
            })
        self.refreshList()



        with open("data_file.json", "w") as fb:
            json.dump(self.data, fb)
            fb.close()

        with ZipFile('data_file.zip', 'w') as myzip:
            myzip.write('data_file.json')

    def on_closing(self):
        print("pidor")
        #if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #    root.destroy()
        answer = mb.askyesno(title="Вопрос", message="Закрыть программу?")
        if answer == True:
            os.remove("data_file.json")
            self.master.destroy()

    def unpacking(self):
        with open("data_file.json", "r") as read_file:
            loadData = json.load(read_file)#[0]
            self.data = loadData

    def FillInList(self):
        self.unpacking()
        for key in self.data:
            tk.l.insert(END, key)

    def refreshList(self):
        tk.l.delete(0,END)
        for key in self.data:
            tk.l.insert(END, key)

    def getPassword(self):
        return tk.password

    def getLogin(self):
        return tk.login


if __name__ == "__main__":
    app = Page()
    app.mainloop()

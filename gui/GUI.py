from tkinter import *
from tkinter import ttk
from drawer import window
root = Tk()

def helloworld():
    print("hello world")
def initGui():
    #Window
    root.title('Drill Drawer')
    root.geometry('800x500')

    #Tabs
    tabControl = ttk.Notebook(root)

    translatorTab = ttk.Frame(tabControl)
    drawerTab = ttk.Frame(tabControl)
    tabControl.add(translatorTab, text ='Drill Translator')
    tabControl.add(drawerTab, text ='Drill Drawer')
    tabControl.pack(expand = 1, fill ="both")

    #Create Window Button
    windowButton = Button(drawerTab, text="Draw Drill", command=(lambda: window.initdrawer()))
    windowButton.pack()
    root.mainloop()
from tkinter import Tk, Frame, Button, Text
from tkinter.filedialog import askopenfilename, asksaveasfilename

##Functions
def newFile(event):
    global path
    if path=="":
        if editorTxt.get('1.0','end-1c')=="":
            pass
        else:
            x=saveAsFile(0)
            if x==None:
                return
    else:
        if editorTxt.get('1.0','end-1c')==open(path, 'r').read():
            pass
        else:
            saveFile(0)
    path=""
    window.title(title)
    editorTxt.delete("1.0","end")

def openFile(event):
    global path
    if path=="":
        if editorTxt.get('1.0','end-1c')=="":
            pass
        else:
            x=saveAsFile(0)
            if x==None:
                return
    else:
        if editorTxt.get('1.0','end-1c')==open(path, 'r').read():
            pass
        else:
            saveFile(0)
    temp=path
    path=askopenfilename(title="Open which mystery?", filetypes=[("All Files", "*.*")])
    if path==temp:
        return
    else:
        file=open(path, "r")
        editorTxt.delete("1.0","end")
        editorTxt.insert("1.0",file.read())
        file.close()
        window.title(title+" - "+path)

def saveAsFile(event):
    global path
    temp=path
    path=asksaveasfilename(title="Where your wizardry lies?", filetypes=[("All Files","*.*")])
    if path==temp:
        return
    else:
        window.title(title+" - "+path)
        file=open(path, "w")
        file.write(editorTxt.get("1.0","end-1c"))
        file.close()

def saveFile(event):
    global path
    file=open(path, "w")
    file.write(editorTxt.get("1.0","end-1c"))
    file.close()

##Root Window
window=Tk()
window.config(bg="black")
window.state("zoomed")
title="Text Editor"
path=""
window.title(title)

##Frames- Menu, EditArea
menuFrm=Frame(master=window, bg="black")
menuFrm.pack()
editorTxt=Text(bg="black", fg="white", font=("Comic Sans MS", 25, "bold"), insertbackground="white")
editorTxt.focus_set()
editorTxt.pack(fill="both", expand=True)

##Menu Design: Buttons
newBtn=Button(master=menuFrm, bg="black", fg="white", text="New")
newBtn.pack(side="left")
openBtn=Button(master=menuFrm, bg="black", fg="white", text="Open")
openBtn.pack(side="left")
saveAsBtn=Button(master=menuFrm, bg="black", fg="white", text="Save As")
saveAsBtn.pack(side="left")
saveBtn=Button(master=menuFrm, bg="black", fg="white", text="Save")
saveBtn.pack(side="left")

##Event Handlers
newBtn.bind("<ButtonRelease-1>", newFile)
window.bind("<Control-n>", newFile)
openBtn.bind("<ButtonRelease-1>", openFile)
window.bind("<Control-o>", openFile)
saveAsBtn.bind("<ButtonRelease-1>", saveAsFile)
saveBtn.bind("<ButtonRelease-1>", saveFile)
window.bind("<Control-s>", saveFile)

##Main Loop
window.mainloop()

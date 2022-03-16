from tkinter import *
import tkinter.messagebox as msgbox

def calcul():
    value = entryvalue.get()
    values=value.split()
    x = int(values[1])/8000 +50
    y = int(values[0])/8000 +50
    label.config(text = "위도 : "+str(round(x,2))+" , 경도 : "+str(round(y,2)))
    entryvalue.delete(0,END)

root=Tk()
root.title("ARK")
root.geometry("270x100")
root.resizable(False,False)

entryvalue = Entry(root,width=30)
entryvalue.pack()
answerbutton = Button(root, padx=10,pady=5,text="계산", command=calcul)
answerbutton.pack()
label=Label(root)
label.pack()

root.mainloop()

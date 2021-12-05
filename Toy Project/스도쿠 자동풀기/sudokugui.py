from tkinter import *

gugu = [[0 for col in range(9)] for row in range(9)]
canx = [[False for col in range(10)] for row in range(10)]
cany = [[False for col in range(10)] for row in range(10)]
cansq=[[[False for i in range(10)] for j in range (10)] for k in range(10)]

solved = False

def solve(cnt):
    global solved,gugu,canx,cany,cansq,entrys
    if(cnt==81):
        solved=True
        return
    x=cnt//9
    y=cnt%9
    if(gugu[x][y]):
        solve(cnt+1)
    else:
        for k in range (1,10):
            if((not canx[x][k]) and (not cany[y][k]) and (not cansq[x//3][y//3][k])):
               canx[x][k]=True
               cany[y][k]=True
               cansq[x//3][y//3][k]=True
               gugu[x][y]=k
               solve(cnt+1)

               if(solved):
                   return

               canx[x][k]=False
               cany[y][k]=False
               cansq[x//3][y//3][k]=False
               gugu[x][y]=0

class Sudoku_entry(Frame):
    def __init__(self,master,row1,column1):
        a=row1//3
        b=column1//3
        if((a+b)%2==0):
            self.e=Entry(root,width=2,font = "Helvetica 18 bold",bg="white")
            self.e.grid(row=row1,column=column1)
            self.e.insert(0,"0")
        else:
            self.e=Entry(root,width=2,font = "Helvetica 18 bold",bg="grey")
            self.e.grid(row=row1,column=column1)
            self.e.insert(0,"0")

    def get(self):
        return int(self.e.get())

def resetall():
    global solved,gugu,canx,cany,cansq,entrys
    solved=False
    for i in range(9):
        for j in range(9):
            gugu[i][j]=0
            entrys[i][j].e.delete(0,END)
            entrys[i][j].e.insert(0,"0")
    for i in range(10):
        for j in range(10):
            canx[i][j]=False
            cany[i][j]=False
            for k in range(10):
                cansq[i][j][k]=False
            
def solve_sudoku():
    global solved,gugu,canx,cany,cansq,entrys
    for i in range(9):
        for j in range(9):
            gugu[i][j]=entrys[i][j].get()
            if(gugu[i][j]):
                canx[i][gugu[i][j]]=True
                cany[j][gugu[i][j]]=True
                cansq[i//3][j//3][gugu[i][j]]=True
    
    solve(0)

    for i in range(9):
        for j in range(9):
            entrys[i][j].e.delete(0,END)
            entrys[i][j].e.insert(0,str(gugu[i][j]))

root=Tk()
root.title("SUDOKU")
root.geometry("270x340")
root.resizable(False,False)

entrys=[]

for i in range (9):
    entryrow=[]
    for j in range (9):
        entryrow.append(Sudoku_entry(root,i,j))
    entrys.append(entryrow)

solve1=Button(root,text="자동해결",padx=5,pady=10,command=solve_sudoku)
solve1.grid(row=9,column=5,columnspan=4,sticky=N+E+W+S)

resetbtn=Button(root,text="리셋",padx=5,pady=10,command=resetall)
resetbtn.grid(row=9,column=0,columnspan=4,sticky=N+E+W+S)

root.mainloop()
            
            

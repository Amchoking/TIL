import time
import tkinter
import tkinter.font
import tkinter.messagebox as msgbox
from tkinter import *
import random

root = Tk()
root.title("반응속도 테스트")
root.geometry("310x400")
root.resizable(False,False)
countdown=99.99
starttime=0
score=30
clickbtn=0
btns=[]
gamestart=False
gamereset=True

def reset_board():
    global countdown, score,clickbtn,btns,gamestart,gamereset
    gamestart=False
    gamereset=True
    score=30
    clickbtn=0
    lefttime.config(text="최고 기록 : "+str(countdown))
    scoreboard.config(text="남은 타일 : "+str(score))
    for i in range (9):
        btns[i].config(bg="green")

def gameover():
    global starttime,countdown
    totaltime=round(time.time()-starttime,2)
    msgbox.showinfo("게임오버",str(totaltime)+"초가 걸렸습니다.")
    reset_board()
    if(countdown>totaltime):
        countdown=totaltime
        lefttime.config(text="최고 기록 : "+str(countdown))

def btn_return0():
    global clickbtn,score,countdown,btns,gamestart
    if(gamestart):
        if(clickbtn==0):
            btns[clickbtn].config(bg="green")
            score=score-1
            if(score==0):
                scoreboard.config(text="남은 타일 : "+str(score))
                gamestart=False
                gameover()
                return
            clickbtn=random.randint(0,8)
            btns[clickbtn].config(bg="red")
            scoreboard.config(text="남은 타일 : "+str(score))
        else:
            score=score+1
            scoreboard.config(text="남은 타일 : "+str(score))

def btn_return1():
    global clickbtn,score,countdown,btns,gamestart
    if(gamestart):
        if(clickbtn==1):
            btns[clickbtn].config(bg="green")
            score=score-1
            if(score==0):
                scoreboard.config(text="남은 타일 : "+str(score))
                gamestart=False
                gameover()
                return
            clickbtn=random.randint(0,8)
            btns[clickbtn].config(bg="red")
            scoreboard.config(text="남은 타일 : "+str(score))
        else:
            score=score+1
            scoreboard.config(text="남은 타일 : "+str(score))

def btn_return2():
    global clickbtn,score,countdown,btns,gamestart
    if(gamestart):
        if(clickbtn==2):
            btns[clickbtn].config(bg="green")
            score=score-1
            if(score==0):
                scoreboard.config(text="남은 타일 : "+str(score))
                gamestart=False
                gameover()
                return
            clickbtn=random.randint(0,8)
            btns[clickbtn].config(bg="red")
            scoreboard.config(text="남은 타일 : "+str(score))
        else:
            score=score+1
            scoreboard.config(text="남은 타일 : "+str(score))

def btn_return3():
    global clickbtn,score,countdown,btns,gamestart
    if(gamestart):
        if(clickbtn==3):
            btns[clickbtn].config(bg="green")
            score=score-1
            if(score==0):
                scoreboard.config(text="남은 타일 : "+str(score))
                gamestart=False
                gameover()
                return
            clickbtn=random.randint(0,8)
            btns[clickbtn].config(bg="red")
            scoreboard.config(text="남은 타일 : "+str(score))
        else:
            score=score+1
            scoreboard.config(text="남은 타일 : "+str(score))

def btn_return4():
    global clickbtn,score,countdown,btns,gamestart
    if(gamestart):
        if(clickbtn==4):
            btns[clickbtn].config(bg="green")
            score=score-1
            if(score==0):
                scoreboard.config(text="남은 타일 : "+str(score))
                gamestart=False
                gameover()
                return
            clickbtn=random.randint(0,8)
            btns[clickbtn].config(bg="red")
            scoreboard.config(text="남은 타일 : "+str(score))
        else:
            score=score+1
            scoreboard.config(text="남은 타일 : "+str(score))

def btn_return5():
    global clickbtn,score,countdown,btns,gamestart
    if(gamestart):
        if(clickbtn==5):
            btns[clickbtn].config(bg="green")
            score=score-1
            if(score==0):
                scoreboard.config(text="남은 타일 : "+str(score))
                gamestart=False
                gameover()
                return
            clickbtn=random.randint(0,8)
            btns[clickbtn].config(bg="red")
            scoreboard.config(text="남은 타일 : "+str(score))
        else:
            score=score+1
            scoreboard.config(text="남은 타일 : "+str(score))

def btn_return6():
    global clickbtn,score,countdown,btns,gamestart
    if(gamestart):
        if(clickbtn==6):
            btns[clickbtn].config(bg="green")
            score=score-1
            if(score==0):
                scoreboard.config(text="남은 타일 : "+str(score))
                gamestart=False
                gameover()
                return
            clickbtn=random.randint(0,8)
            btns[clickbtn].config(bg="red")
            scoreboard.config(text="남은 타일 : "+str(score))
        else:
            score=score+1
            scoreboard.config(text="남은 타일 : "+str(score))

def btn_return7():
    global clickbtn,score,countdown,btns,gamestart
    if(gamestart):
        if(clickbtn==7):
            btns[clickbtn].config(bg="green")
            score=score-1
            if(score==0):
                scoreboard.config(text="남은 타일 : "+str(score))
                gamestart=False
                gameover()
                return
            clickbtn=random.randint(0,8)
            btns[clickbtn].config(bg="red")
            scoreboard.config(text="남은 타일 : "+str(score))
        else:
            score=score+1
            scoreboard.config(text="남은 타일 : "+str(score))

def btn_return8():
    global clickbtn,score,countdown,btns,gamestart
    if(gamestart):
        if(clickbtn==8):
            btns[clickbtn].config(bg="green")
            score=score-1
            if(score==0):
                scoreboard.config(text="남은 타일 : "+str(score))
                gamestart=False
                gameover()
                return
            clickbtn=random.randint(0,8)
            btns[clickbtn].config(bg="red")
            scoreboard.config(text="남은 타일 : "+str(score))
        else:
            score=score+1
            scoreboard.config(text="남은 타일 : "+str(score))

def game_start():
    global btns, countdown,score,clickbtn,gamestart,starttime,gamereset
    if(gamereset):
        gamestart=True
        gamereset=False
        clickbtn=random.randint(0,8)
        btns[clickbtn].config(bg="red")
        starttime=time.time()

def howtoplay():
    msgbox.showinfo("게임 방법","최대한 빠르게 빨간색으로 변하는 버튼 30개를 눌러주세요!\n틀릴때마다 남은 타일이 1개씩 늘어납니다!")

def whomade():
    msgbox.showinfo("만든 사람","유상혁 in ROKA")    

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="게임 방법",command=howtoplay)
menu_file.add_command(label="만든 사람",command=whomade)
menu_file.add_separator()
menu_file.add_command(label="게임 종료",command=root.quit)
menu.add_cascade(label="게임 메뉴",menu=menu_file)

#초기 세팅
btns.clear()
font=tkinter.font.Font(family="맑은 고딕", size=10, slant="italic")
frame_score = Frame(root,relief="solid",bd=1)
frame_score.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
lefttime=Label(frame_score,text="최고 기록 : "+str(countdown),width=20,height=2,font=font)
lefttime.pack(side="left")
scoreboard=Label(frame_score,text="남은 타일 : "+str(score),width=20,height=2,font=font)
scoreboard.pack(side="right")
btns.append(Button(root,text="",width=5,height=5,command=btn_return0,bg="green"))
btns.append(Button(root,text="",width=5,height=5,command=btn_return1,bg="green"))
btns.append(Button(root,text="",width=5,height=5,command=btn_return2,bg="green"))
btns.append(Button(root,text="",width=5,height=5,command=btn_return3,bg="green"))
btns.append(Button(root,text="",width=5,height=5,command=btn_return4,bg="green"))
btns.append(Button(root,text="",width=5,height=5,command=btn_return5,bg="green"))
btns.append(Button(root,text="",width=5,height=5,command=btn_return6,bg="green"))
btns.append(Button(root,text="",width=5,height=5,command=btn_return7,bg="green"))
btns.append(Button(root,text="",width=5,height=5,command=btn_return8,bg="green"))

for i in range (9):
    btns[i].grid(row=i//3+1, column=i%3,sticky=N+E+W+S,padx=5,pady=5)
reset=Button(root,text="Reset",command=reset_board,height=2)
reset.grid(row=4,column=0,sticky=N+E+W+S,padx=10,pady=10)
start=Button(root,text="Start",command=game_start,height=2)
start.grid(row=4,column=2,sticky=N+E+W+S,padx=10,pady=10)
    
root.config(menu=menu)
root.mainloop()

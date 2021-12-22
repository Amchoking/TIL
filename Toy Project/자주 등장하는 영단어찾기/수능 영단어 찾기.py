import re
import operator
from tkinter import *
import tkinter.messagebox as msgbox
import webbrowser

dictionary={}
bestword_dictionary={}
bestword_count={}

def make_window():
    global window
    window = Tk()
    window.title("수능 영단어 찾기")
    window.geometry("900x500")

def make_dictionary():
    global list_check, list_ban
    for i in list_check:
        if not(i in list_ban):
            if(i in dictionary):
                dictionary[i]=dictionary[i]+1
            else:
                dictionary[i]=1

def reset_window():
    global window
    mylist = window.grid_slaves()
    for i in mylist:
        i.destroy()

def end_title():
    global window
    reset_window()
    end_label = Label(window,text="기록이 종료되었습니다!",font="Helvetica 30 bold")
    end_label.grid(row=0,column=0,padx=100,pady=100)

def right_wrong(i):
    global word,meaning_entry,word_count
    meaning = meaning_entry.get()
    if(meaning == bestword_dictionary[word]):
        msgbox.showinfo("정답","정답입니다!")
        check = msgbox.askquestion("단어 삭제?","이 단어를 단어장에서 삭제합니까?")
        if (check=="yes"):
            baned_file = open("baned.txt","a")
            baned_file.write(" "+word)
            baned_file.close()
            print_dictionary(i+1)
            return
    else:
        msgbox.showerror("오답","정답은 "+bestword_dictionary[word]+"입니다.")
        
    save_file = open("bestword.txt","a")
    save_str = word+" "+bestword_dictionary[word]+" "+str(word_count+bestword_count[word])+"\n"
    save_file.write(save_str)
    save_file.close()
    print_dictionary(i+1)

def word_test(i):
    global window,word,word_count,meaning_entry
    main_label = Label(window,text="이미 "+str(word_count+bestword_count[word])+"번 나온 단어입니다.\n뜻을 입력해주세요!",font="Helvetica 30 bold")
    main_label.grid(row=0,column=0,sticky=N+E+S+W,padx=100,pady=50)
    word_label = Label(window,text=word,font="Helvetica 20")
    word_label.grid(row=1,column=0,sticky=N+E+S+W,padx=100,pady=20)
    meaning_entry = Entry(window,width=30,font="Helvetica 15")
    meaning_entry.grid(row=2,column=0,sticky=N+E+S+W,padx=100,pady=20)
    ok_btn=Button(window,text="확인",font="Helvetica 15",command=lambda :right_wrong(i))
    ok_btn.grid(row=3,column=0,sticky=N+E+S+W,padx=100,pady=20)

def add_dictionary(i):
    global word,word_count,add_meaning_entry
    meaning=add_meaning_entry.get()
    if(meaning=""):
        msgbox.showerror("에러","단어의 뜻을 입력해주세요!")
        return
    save_file = open("bestword.txt","a")
    save_str = word+" "+meaning+" "+str(word_count)+"\n"
    save_file.write(save_str)
    save_file.close()
    print_dictionary(i+1)

def search_word():
    global word
    webbrowser.open("https://www.google.com/search?q="+word+"뜻")

def ban_dictionary(i):
    global word
    baned_file = open("baned.txt","a")
    baned_file.write(" "+word)
    baned_file.close()
    print_dictionary(i+1)

def word_check(i):
    global window, word, word_count,add_meaning_entry
    main_label = Label(window,text="처음 등장한 단어입니다!("+str(word_count)+"번)",font="Helvetica 30 bold")
    main_label.grid(row=0,column=0,columnspan=3,sticky=N+E+S+W,padx=100,pady=50)
    word_label = Label(window,text=word,font="Helvetica 20")
    word_label.grid(row=1,column=0,columnspan=3,sticky=N+E+S+W,padx=100,pady=20)
    add_meaning_entry=Entry(window,width=30,font="Helvetica 15")
    add_meaning_entry.grid(row=2,column=0,columnspan=3,sticky=N+E+S+W,padx=100,pady=20)
    add_btn=Button(window,text="단어장에 추가O",font="Helvetica 15",command=lambda: add_dictionary(i))
    add_btn.grid(row=3,column=0,sticky=N+E+S+W,padx=10,pady=10)
    delete_btn=Button(window,text="단어장에 추가X",font="Helvetica 15",command= lambda: ban_dictionary(i))
    delete_btn.grid(row=3,column=1,sticky=N+E+S+W,padx=10,pady=10)
    search_btn = Button(window,text="뜻 검색하기",font="Helvetica 15",command=search_word)
    search_btn.grid(row=3,column=2,sticky=N+E+S+W,padx=10,pady=10)


def print_dictionary(i):
    global window, sorted_dict, word, word_count
    if(i==len(sorted_dict)):
        end_title()
        return
    reset_window()
    word = sorted_dict[i][0] 
    word_count = sorted_dict[i][1]
    if (word in bestword_dictionary):
        word_test(i)
    else:
        word_check(i)
    

def make_sorted_dictionary():
    global sorted_dict
    sorted_dict= sorted(dictionary.items(), key=operator.itemgetter(1))
    sorted_dict.reverse()

def get_file():
    global list_check,list_ban,list_bestword
    baned_file = open("baned.txt","r")
    list_ban = baned_file.read().split()
    baned_file.close()
    bestword_file = open("bestword.txt","r")
    save_bestword = bestword_file.read().split("\n")
    for i in save_bestword:
        if(i==""):
            break
        bestword_check = i.split()
        if bestword_check[0] in bestword_dictionary:
            if (bestword_count[bestword_check[0]]<bestword_check[2]):
                bestword_count[bestword_check[0]]=int(bestword_check[2])
        else:
            bestword_dictionary[bestword_check[0]]=bestword_check[1]
            bestword_count[bestword_check[0]]=int(bestword_check[2])
    bestword_file.close()
    file_open = open("english.txt","r")
    file_save = file_open.read().split()
    file_open.close()
    list_check=[]
    for i in file_save:
        text=re.sub('[^a-zA-Z]',' ',i).strip()
        textcheck=text.split()
        for i in textcheck:
            if(i!=""):
                list_check.append(i.lower())

def main():
    make_window()
    get_file()
    make_dictionary()
    make_sorted_dictionary()
    print_dictionary(0)

if __name__ == "__main__":
    main()
    mainloop()

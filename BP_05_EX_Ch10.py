1.
from tkinter import Tk, Label, Button  #tkinter 라이브러리 호출 전부 사용

def greet():
 print("파이썬에 오신 것을 환영합니다. ")

window = Tk()
label = Label(window, text="간단한 GUI 프로그램!")
label.pack()

greet_button = Button(window, text="환영합니다.", command=greet)
greet_button.pack()

close_button = Button(window, text="종료", command=window.quit)
close_button.pack()

window.mainloop()
2.
from tkinter import *

total=0


def add():   # 더하기 함수
    global total  #글로벌 전역
    total=total+int(entry.get())  # 추출 메소드 정수형으로 형변환
    SumNum.config(text=str(total))

def minus():  # 빼기 함수
    global total
    total=total-int(entry.get())
    SumNum.config(text=str(total))

def reset():  # 초기화 함수
    global total
    total=0
    SumNum.config(text=str(total))

window=Tk()    #tkinter 호출


total=0

NowSum=Label(window,text="현재 합계: ")
SumNum=Label(window,text=total)
NowSum.grid(row=0,column=0)
SumNum.grid(row=0,column=1)

entry=Entry(window)
entry.grid(row=1, column=0, columnspan=3)

addbutt=Button(window,text='더하기(+)', command=add)
minusbutt=Button(window,text='빼기(-)', command=minus)
resetbutt=Button(window,text='reset', command=reset)
#각 버튼 생성 후 클릭이벤트 시 연결되는 함수 지정
addbutt.grid(row=2,column=0)
minusbutt.grid(row=2,column=1)
resetbutt.grid(row=2,column=2)
#버튼 그리드 (위치)
window.mainloop()
3.
import random
from tkinter import *  #Tkinter 라이브러리 호출 모두 사용

window = Tk()  #tkinter 정의
secret_number = random.randint(1, 100) # 랜덤 숫자 1~100사이 생성
guess = None
num_guesses = 0 #num 초기화

def guess_number(): #함수 생성
    global num_guesses
    guess = int(entry.get())  # 추출 메소드 정수형으로 형변환
    num_guesses += 1
    if guess == secret_number:
        message = "축하합니다!!"
    elif guess < secret_number:
        message = "너무 낮아요!!"
    else:
        message = "너무 높아요!!"
    label['text']= message
     # 조건문 각각 조건에 부합 시 해당 문구 라벨에 출력
def reset():  #초기화 함수 생성
    global num_guesses
    entry.delete(0, END) # 끝 숫자 삭제
    secret_number = random.randint(1, 100)
    guess = 0
    num_guesses = 0
    message = "1부터 100사이의 숫자를 추측하시오"
    label['text']= message
    
message = "1부터 100사이의 숫자를 추측하시오"
label = Label(window, text=message)
entry = Entry(window)

guess_button = Button(window, text="숫자를 입력", command=guess_number)
reset_button = Button(window, text="게임을 다시 실행", command=reset)

label.grid(row=0, column=0, columnspan=2, sticky=W+E)
entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
guess_button.grid(row=2, column=0)
reset_button.grid(row=2, column=1)

window.mainloop() #창 유지 
4.
from tkinter import *

def do_convert():
 inch_val = float(cvt_from.get())
 centimeters_val = inch_val * 2.54
 cvt_to.set('%s 센티미터' % centimeters_val)

root = Tk()
cvt_from = StringVar()
cvt_to = StringVar()

lbl = Label(root, text='인치를 센티미디로 변환하는 프로그램:')
lbl.grid(row=0, column=0, columnspan=2)
from_lbl = Label(root, text='인치를 입력하시오:')
from_lbl.grid(row=1, column=0)
from_entry = Entry(root, textvariable=cvt_from)
from_entry.grid(row=1, column=1)

to_lbl = Label(root, text='변환결과:')
to_lbl.grid(row=2, column=0)
result_lbl = Label(root,
 textvariable=cvt_to)
result_lbl.grid(row=2, column=1)

convert_btn = Button(root,
 text='변환!', command=do_convert)
convert_btn.grid(row=3, column=1) #그리드
#버튼 클릭 시 인치 변환 함수로 실행
root.mainloop()
5.
from tkinter import *
fields = '이름', '직업', '국적' #상단 라벨 생성

def fetch(entries):
  for entry in entries:
     field = entry[0]
     text = entry[1].get()
     print('%s: "%s"' % (field, text))
def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field)
      ent = Entry(row)
      row.pack(side=TOP, fill=X)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
    return entries
root = Tk()
ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: fetch(e)))
b1 = Button(root, text='보여주기',
     command=(lambda e=ents: fetch(e)))
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(root, text='종료하기', command=root.quit)
b2.pack(side=LEFT, padx=5, pady=5)
root.mainloop()
6.
from random import *
from tkinter import *

# 선택 하는 부분
def user_choice_rock():
    user_choice = "rock"
    turn(user_choice)
    user_image.configure(image=rock_image)
def user_choice_paper():
    user_choice = "paper"
    turn(user_choice)
    user_image.configure(image=paper_image)
def user_choice_scissors():
    user_choice = "scissors"
    turn(user_choice)
    user_image.configure(image=scissors_image)
    
# 게임부분
def turn(user_choice):
    oppo = ['rock', 'paper', 'scissors']
    oppo_choice=oppo[randint(0,2)]
    if(oppo_choice=='rock'):
        oppo_image.configure(image=rock_image)
        if(user_choice=='paper'):
            turn_result.configure(text="사용자 승!", fg="green")
            compare.configure(text=">>>>>")
        elif(user_choice=='scissors'):
            turn_result.configure(text="컴퓨터 승!", fg="red")
            compare.configure(text="<<<<<")
        else:
            turn_result.configure(text="무승부", fg="gray")
            compare.configure(text="=====")

    elif(oppo_choice=='paper'):
        oppo_image.configure(image=paper_image)
        if(user_choice=='scissors'):
            turn_result.configure(text="사용자 승!", fg="green")
            compare.configure(text=">>>>>")
        elif(user_choice=='rock'):
            turn_result.configure(text="컴퓨터 승!", fg="red")
            compare.configure(text="<<<<<")
        else:
            turn_result.configure(text="무승부", fg="gray")
            compare.configure(text="=====")

    elif(oppo_choice=='scissors'):
     oppo_image.configure(image=scissors_image)
     if(user_choice=='rock'):
         turn_result.configure(text="사용자 승!", fg="green")
         compare.configure(text=">>>>>")
     elif(user_choice=='paper'):
         turn_result.configure(text="컴퓨터 승!", fg="red")
         compare.configure(text="<<<<<")
     else:
         turn_result.configure(text="무승부", fg="gray")
         compare.configure(text="=====")

# 메인 프로그램
main_window = Tk()
rock_button = Button(main_window, width=20, text="바위", justify=CENTER,
command=user_choice_rock, activebackground='black', activeforeground='white')
paper_button = Button(main_window, width=20, text="보", justify=CENTER,
command=user_choice_paper, activebackground='black', activeforeground='white')
scissors_button = Button(main_window, width=20, text="가위", justify=CENTER,
command=user_choice_scissors, activebackground='black', activeforeground='white')
rock_image = PhotoImage(file="rock.png")
paper_image = PhotoImage(file="paper.png")
scissors_image = PhotoImage(file="scissors.png")
user_image = Label(text="사용자", image=rock_image)
user_image.image = rock_image
compare = Label(main_window, justify=CENTER, font=("Helvetica", 30))
oppo_image = Label(text="컴퓨터",image=paper_image)
oppo_image.image = paper_image
turn_result = Label(main_window, width=20, justify=CENTER, font=("Helvetica", 20))

# 그리드 생성
rock_button.grid(row=5, column=1)
paper_button.grid(row=5, column=2)
scissors_button.grid(row=5, column=3)
user_image.grid(row=3, column=1)
compare.grid(row=3, column=2)
oppo_image.grid(row=3, column=3)
turn_result.grid(row=4, column=2)

# GUI화면 루프처리
main_window.mainloop()
*로그인하는 프로그램
from tkinter import *

window = Tk()
label1 = Label(window, text="로그인 하세요!!!", font=("Helvetica", 20))
label1.pack()
label2 = Label(window, text="아이디")
label2.pack()
entry1 = Entry(window)
entry1.pack()
label2 = Label(window, text="패스워드")
label2.pack()
entry2 = Entry(window)
entry2.pack()
button1 = Button(window, text="로그인")
button1.pack()
window.mainloop()

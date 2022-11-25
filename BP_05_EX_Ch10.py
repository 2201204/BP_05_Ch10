1.
from tkinter import Tk, Label, Button

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


def add():
    global total
    total=total+int(entry.get())
    SumNum.config(text=str(total))

def minus():
    global total
    total=total-int(entry.get())
    SumNum.config(text=str(total))

def reset():
    global total
    total=0
    SumNum.config(text=str(total))

window=Tk()


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
addbutt.grid(row=2,column=0)
minusbutt.grid(row=2,column=1)
resetbutt.grid(row=2,column=2)

window.mainloop()
3.
import random
from tkinter import *

window = Tk()
secret_number = random.randint(1, 100)
guess = None
num_guesses = 0

def guess_number():
    global num_guesses
    guess = int(entry.get())
    num_guesses += 1
    if guess == secret_number:
        message = "축하합니다!!"
    elif guess < secret_number:
        message = "너무 낮아요!!"
    else:
        message = "너무 높아요!!"
    label['text']= message
def reset():
    global num_guesses
    entry.delete(0, END)
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

window.mainloop()
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
convert_btn.grid(row=3, column=1)
root.mainloop()
5.
from tkinter import *
fields = '이름', '직업', '국적'

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

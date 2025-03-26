import tkinter as tk
from PIL import Image,ImageTk
import random
import sys
import os
window=tk.Tk()
window.title('the numbers baseball')
if getattr(sys,'frozen',False):base_path=sys._MEIPASS
else:base_path=os.path.abspath('.')
image_path=os.path.join(base_path,'baseball.png')
image=Image.open(image_path)
photo=ImageTk.PhotoImage(image)
window.iconphoto(True,photo)
window.geometry('500x500')
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
answer=random.sample(range(1,10),3)
desc=tk.Label(window,text='1부터 9까지 3자리 숫자를 입력해주세요')
desc.pack()
entry=tk.Entry(window)
entry.pack()
def oncl():
    term=[]
    strike=0
    ball=0
    for digit in str(entry.get()):term.append(int(digit))
    for i in range(len(term)):
        if answer[i]==term[i]:strike+=1
        elif term[i] in answer:ball+=1
    newone=tk.Label(window,text=f'{entry.get()} {strike}S{ball}B',font=('arial',20))
    newone.pack()
    if strike==3:
        winn=tk.Label(window,text='you win',font=('arial',30,'bold'),fg='red')
        winn.pack()
    entry.delete(0,tk.END)
button=tk.Button(window,text='button',command=oncl,cursor='hand2')
button.pack()
label=tk.Label(window)
label.pack()
window.mainloop()
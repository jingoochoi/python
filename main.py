import tkinter as tk
window=tk.Tk()
window.title('python')
window.geometry('500x500')
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
entry=tk.Entry(window)
entry.pack()
def oncl():
    label.config(text=entry.get())
    entry.delete(0,tk.END)
    window.focus_force()
button=tk.Button(window,text='button',command=oncl,cursor='hand2')
button.pack()
label=tk.Label(window)
label.pack()
window.mainloop()
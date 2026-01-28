# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

from tkinter import *

def button_clicked():
    print("I am clicked")
    new_text = input.get()
    my_level.config(text=new_text)


window = Tk()
window.title("My First GUI")
window.geometry("600x400") #also window.minsize(widt=500,height=300)
window.config(padx=60, pady=60)
#level
my_level = Label(text="I am a label", font=("Arial", 24, "bold"))
my_level.config(text="New Text")
my_level.grid(column=0, row=0)
my_level.config(padx=20, pady=20)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me", command=button_clicked)
new_button.grid(column=2, row=0)

input = Entry(width=20)
print(input.get())
input.grid(column=3, row=3)

window.mainloop()
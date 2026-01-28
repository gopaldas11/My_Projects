from tkinter import *
#Creating a new window and configuration .
window = Tk()
window.title("Widget Examples")
window.geometry("500x500")

#Now creating Levels
label = Label(text="This is Old text")
label.config(text="This is New text")
label.pack()
# Now Buttoms
def action():
    print("Do something")

#Call action when pressed
button = Button(text="Click Me",command=action)
button.pack()

#Now entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Example of multiline text entry")
print(entry.get())
entry.pack()
#text
text = Text(width=30, height=5)
text.focus() #Puts cursor in toolbox
text.insert(END, "Example of multiline text entry")   #Add some text to begain with
#get's current value in textbox at line 1 character 0.
print(text.get("1.0",END))
text.pack()

#spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get)

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#scale , # call the current scale value
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()
#checkbutton
def checkbutton_used():
    #print 1 if On button checked otherwise 0
    print(checked_state.get)

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()
#readio button
def radio_used():
    print(radio_state.get)
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", variable=radio_state, value=1, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", variable=radio_state, value=2, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["apple", "banana", "cherry"]

for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()



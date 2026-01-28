from tkinter import *
# def button_clicked():
#     new_text = input.get()
#     my_level.config(text=new_text)
#
#
# window = Tk()
# window.title("Mile to Km Converter")
# window.geometry("400x200")
# window.config(padx=20, pady=20)
#
# my_level = Label(text="I am a label", font=("Arial", 11))
# my_level.config(text="Is equal to : ")
# my_level.grid(column=0, row=1)
#
# my_level2 = Label(text="I am a label", font=("Arial", 11))
# my_level2.config(text="Miles")
# my_level2.grid(column=2, row=0)
#
# my_level3 = Label(text="I am a label", font=("Arial", 11))
# my_level3.config(text="Km")
# my_level3.grid(column=2, row=1)
#
# input = Entry(width=20)
# print(input.get())
# input.grid(column=1, row=0)
#
# input = Entry(width=20)
# print(input.get())
# input.grid(column=1, row=1)
#
# button = Button(text="Calculate", command=button_clicked)
# button.grid(column=1, row=2)
#
# window.mainloop()


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=25)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934)
    km_result_label.config(text=f"{km}")


miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

miles_lavel = Label(text="Miles")
miles_lavel.grid(column=2, row=0)

is_equel_label = Label(text="Is equal to : ")
is_equel_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_lavel = Label(text="Km")
km_lavel.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()



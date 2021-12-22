from tkinter import *
from tkinter import ttk

def sum():
    print(user_number_1.get() + user_number_2.get())

def difference():
    print(user_number_1.get() - user_number_2.get())

def multiply():
    print(user_number_1.get() * user_number_2.get())

def divide():
    if user_number_2.get() == 0:
        print('It is unreal to divide by zero')
    else:
        print(user_number_1.get() / user_number_2.get())


root = Tk()

root.title('Calculator')

first_frame = ttk.Frame(root, heigh=500, width=500, relief='solid')
first_frame.grid()

input_frame = ttk.Frame(first_frame, padding=(5, 5, 10, 10))
input_frame.grid()

label = ttk.Label(input_frame, text='Put your numbers')
label.grid()

user_number_1 = IntVar()

entery_frame = ttk.Entry(input_frame, textvariable=user_number_1)
entery_frame.grid()

user_number_2 = IntVar()

entery_frame = ttk.Entry(input_frame, textvariable=user_number_2)
entery_frame.grid()

end_frame = ttk.Frame(input_frame, textvariable=divide())
end_frame.grid(sticky='E')


buttons_frame = ttk.Frame(root, padding=(10, 5), relief='solid')
buttons_frame.grid()

sum_button = ttk.Button(buttons_frame, text='+', command=sum)
sum_button.grid()

dif_button = ttk.Button(buttons_frame, text='-', command=difference)
dif_button.grid()

div_button = ttk.Button(buttons_frame, text='/', command=divide)
div_button.grid()

mult_button = ttk.Button(buttons_frame, text='x', command=multiply)
mult_button.grid()

root.mainloop()

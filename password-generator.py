import random
from tkinter import *
from tkinter import messagebox


capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                   'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                 'x', 'y', 'z']
symbols = ['!', '”', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/',
           ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{',
           '|', '~']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                   'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['!', '”', '#', '$', '%', '&', '(', ')', '*',
           '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
           '[', ']', '^', '_', '`', '{', '|', '~']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def sma_rand():
    sma_rand = random.choice(small_letters)
    return sma_rand


def cap_rand():
    cap_rand = random.choice(capital_letters)
    return cap_rand


def symbl_rand():
    symbol = random.choice(symbols)
    return symbol


def numb_rand():
    numb_rand = random.choice(numbers)
    return numb_rand


def password_generator():
    if pwd_len.get() == '':
        messagebox.showerror(
            message='enter the number of letters', title='invalid data')
        window.destroy()
    else:
        try:
            int(pwd_len.get())
        except:
            messagebox.showerror(
                message='enter number only', title='invalid data')
            window.destroy()
        else:
            master_pwd = ''
            if int(pwd_len.get()) <= 20:
                for i in range(0, int(pwd_len.get())):
                    val = random.choice(
                        [0, val1.get(), val2.get(), val3.get()])
                    switcher = {0: sma_rand(), 1: cap_rand(),
                                2: numb_rand(), 3: symbl_rand()}
                    master_pwd = master_pwd + switcher.get(val)
                    Label(window, text='the password is: ',
                          fg='green').place(x=100, y=250)
                    t1 = Text(window, width=20, height=1)
                    t1.insert(INSERT, master_pwd)
                    t1.place(x=200, y=250)
            else:
                Label(window, text='the password min size is 20!',
                      fg='red').place(x=100, y=250)


def main():
    global val1
    global val2
    global val3
    global pwd_len
    global window
    # basic gui window
    window = Tk()
    window.geometry('400x350')
    window.title('password generator')
    # labels for entry part
    # Title:
    Label(window, text='password generator',
          font='TimesNewRoman 18 bold', fg='blue').place(x=100, y=0)
    ###
    Label(window, text='enter password length:').place(x=30, y=80)
    # entry widget
    pwd_len = Entry(window)
    pwd_len.place(x=160, y=80)
    # check buttons for addition of letters,symbols
    val1 = IntVar()
    val2 = IntVar()
    val3 = IntVar()
    check_b1 = Checkbutton(window, text='capital letters',
                           var=val1, onvalue=1, offvalue=0).place(x=160, y=100)
    check_b2 = Checkbutton(window, text='numbers', var=val2,
                           onvalue=2, offvalue=0).place(x=160, y=125)
    check_b3 = Checkbutton(window, text='symbols', var=val3,
                           onvalue=3, offvalue=0).place(x=160, y=150)
    Button(window, text='Done', activebackground='green',
           command=password_generator).place(x=180, y=210)
    window.mainloop()


main()

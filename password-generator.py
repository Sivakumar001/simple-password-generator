import random
import string
from tkinter import *
from tkinter import messagebox


def sma_rand():
    sma_rand = random.choice(string.ascii_lowercase)
    return sma_rand


def cap_rand():
    cap_rand = random.choice(string.ascii_uppercase)
    return cap_rand


def symbl_rand():
    symbol = random.choice(string.punctuation)
    return symbol


def numb_rand():
    numb_rand = random.choice(string.digits)
    return numb_rand


def password_generator():
    global master_pwd
    if pwd_len.get() == '':
        messagebox.showerror(
            message='enter the number of letters', title='invalid data')
        window.destroy()
    else:
        try:
            int(pwd_len.get())
        except Exception:
            messagebox.showerror(message='enter number only',
                                 title='invalid data')
            pwd_len.delete(0, END)

        else:
            master_pwd = ''
            if int(pwd_len.get()) <= 20:
                for i in range(0, int(pwd_len.get())):
                    val = random.choice([0, val1.get(), val2.get(),
                                         val3.get()])
                    switcher = {0: sma_rand(), 1: cap_rand(),
                                2: numb_rand(), 3: symbl_rand()}
                    master_pwd = master_pwd + switcher.get(val)
                l1 = Label(window, text='the password is: ',
                           fg='green')
                l1.place(x=100, y=250)
                t1 = Text(window, width=20, height=1)
                t1.insert(INSERT, master_pwd)
                t1.place(x=200, y=250)
            else:
                error = Label(window, text='the password min size is 20!',
                              fg='red')
                error.place(x=100, y=250)
                error.after(1000, lambda: error.destroy())


def copy():
    global master_pwd
    if master_pwd.isascii:
        window.clipboard_clear()
        window.clipboard_append(master_pwd)
        window.update()
        master_pwd = ''
    else:
        messagebox.showerror(title='no input', text='enter the input first')


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
    Checkbutton(window, text='capital letters',
                var=val1, onvalue=1, offvalue=0).place(x=160, y=100)
    Checkbutton(window, text='numbers', var=val2,
                onvalue=2, offvalue=0).place(x=160, y=125)
    Checkbutton(window, text='symbols', var=val3,
                onvalue=3, offvalue=0).place(x=160, y=150)
    Button(window, text='Done', activebackground='green',
           command=password_generator).place(x=180, y=210)
    Button(window, text='copy', foreground='blue',
           command=copy).place(x=220, y=210)
    window.mainloop()


main()

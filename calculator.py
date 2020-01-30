from tkinter import *

cal = Tk()
cal.title("Calculator")
text_Input = StringVar()
cal.resizable(0, 0)

# global vars
last_number = 0
current_number = 0
kept_result = 0
new_number = True
last_action = "="
level_2 = False
level_2_action = ""
keep = ["last action", 0, 0, 0, "level2 action", False]

# tk entry.
# font = font options for the display
# textVariable = retrieves what you type - StringVar class
# bd = border
# bg = background
text_view = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, width=15, bd=10, insertwidth=4,
                  bg="white", justify='right')
text_view.grid(row=0, column=1, columnspan=4)


# Removes numbers once the entry fills up
def remove_extra():
    if len(text_view.get()) > 14:
        text_view.delete(0)


# adds the numbers to the vars
def add_number(n):
    global new_number, last_number, current_number
    if not new_number:
        current_number *= 10
        current_number += n
    else:
        last_number = current_number
        current_number = n
    new_number = False
    remove_extra()


# pressing 1
def press_1():
    text_view.insert(len(text_view.get()), "1")
    add_number(1)


# pressing 2
def press_2():
    text_view.insert(len(text_view.get()), "2")
    add_number(2)


# pressing 3
def press_3():
    text_view.insert(len(text_view.get()), "3")
    add_number(3)


# pressing 4
def press_4():
    text_view.insert(len(text_view.get()), "4")
    add_number(4)


# pressing 5
def press_5():
    text_view.insert(len(text_view.get()), "5")
    add_number(5)


# pressing 6
def press_6():
    text_view.insert(len(text_view.get()), "6")
    add_number(6)


# pressing 7
def press_7():
    text_view.insert(len(text_view.get()), "7")
    add_number(7)


# pressing 8
def press_8():
    text_view.insert(len(text_view.get()), "8")
    add_number(8)


# pressing 9
def press_9():
    text_view.insert(len(text_view.get()), "9")
    add_number(9)


# pressing 0
def press_0():
    if text_view.get() != "0":
        text_view.insert(len(text_view.get()), "0")
        add_number(0)


# Calculating and adding things up. the "magic" of it
def calculate():
    global kept_result, level_2, current_number
    print("Cal start")
    print("Kept: ", kept_result)
    print("Last: ", last_number)
    print("Current: ", current_number)
    if level_2:
        level_2 = False
        print("level 2 action in cal")
        if last_action == "-":
            kept_result += last_number
        elif last_action == "+":
            kept_result -= last_number
        elif last_action == "=":
            kept_result = last_number

        if level_2_action == "*":
            print("level 2 action in cal - mul")
            current_number *= last_number
        elif level_2_action == "/":
            print("level 2 action in cal - div")
            current_number = last_number / current_number

        calculate()

    elif last_action == "-":
        kept_result -= current_number
    elif last_action == "+":
        kept_result += current_number
    elif last_action == "=":
        kept_result = current_number
    print("Cal end")
    print("Kept: ", kept_result)
    print("Last: ", last_number)
    print("Current: ", current_number)


def press_plus():
    global new_number, last_action
    if (text_view.get() != "") != new_number:
        text_view.insert(len(text_view.get()), "+")
        new_number = True
        calculate()
        last_action = "+"
        remove_extra()


def press_sub():
    global new_number, last_action
    if (text_view.get() != "") != new_number:
        text_view.insert(len(text_view.get()), "-")
        new_number = True
        calculate()
        last_action = "-"
        remove_extra()


def press_mul():
    global level_2, new_number, level_2_action
    if (text_view.get() != "") != new_number:
        text_view.insert(len(text_view.get()), "*")
        calculate()
        new_number = True
        level_2 = True
        level_2_action = "*"
        remove_extra()


def press_div():
    global level_2, new_number, level_2_action
    if (text_view.get() != "") != new_number:
        text_view.insert(len(text_view.get()), "/")
        calculate()
        new_number = True
        level_2 = True
        level_2_action = "/"
        remove_extra()


def open_brackets():
    global last_number, current_number, kept_result, new_number, last_action, level_2, level_2_action
    text_view.insert(len(text_view.get()), "(")
    keep[0] = last_action
    keep[1] = last_number
    keep[2] = current_number
    keep[3] = kept_result
    keep[4] = level_2_action
    keep[5] = level_2

    last_number = 0
    current_number = 0
    kept_result = 0
    new_number = True
    last_action = "="
    level_2 = False
    level_2_action = ""
    remove_extra()


def close_brackets():
    global last_number, current_number, kept_result, new_number, last_action, level_2, level_2_action
    calculate()
    text_view.insert(len(text_view.get()), ")")
    last_action = keep[0]
    last_number = keep[1]
    current_number = kept_result
    kept_result = keep[3]
    level_2_action = keep[4]
    level_2 = keep[5]
    if last_action == "=":
        last_number = kept_result
    remove_extra()


def press_end():
    global kept_result, last_number, current_number, last_action
    calculate()
    text_view.delete(first=0, last=len(text_view.get()))
    text_view.insert(0, kept_result)
    print(kept_result)
    current_number = kept_result
    kept_result = 0
    last_number = 0
    last_action = "="


def clear():
    global last_number, current_number, kept_result, new_number, last_action, level_2, level_2_action
    text_view.delete(first=0, last=len(text_view.get()))
    last_number = 0
    current_number = 0
    kept_result = 0
    new_number = True
    last_action = "="
    level_2 = False
    level_2_action = ""


# 0 - 9 buttons
button_1 = Button(cal, text='1', width=10, command=press_1)
button_1.grid(row=2, column=1)
button_2 = Button(cal, text='2', width=10, command=press_2)
button_2.grid(row=2, column=2)
button_3 = Button(cal, text='3', width=10, command=press_3)
button_3.grid(row=2, column=3)
button_4 = Button(cal, text='4', width=10, command=press_4)
button_4.grid(row=3, column=1)
button_5 = Button(cal, text='5', width=10, command=press_5)
button_5.grid(row=3, column=2)
button_6 = Button(cal, text='6', width=10, command=press_6)
button_6.grid(row=3, column=3)
button_7 = Button(cal, text='7', width=10, command=press_7)
button_7.grid(row=4, column=1)
button_8 = Button(cal, text='8', width=10, command=press_8)
button_8.grid(row=4, column=2)
button_9 = Button(cal, text='9', width=10, command=press_9)
button_9.grid(row=4, column=3)
button_0 = Button(cal, text='0', width=10, command=press_0)
button_0.grid(row=5, column=2)

# add button
button_plus = Button(cal, text='+', width=10, command=press_plus)
button_plus.grid(row=3, column=4)
# sub button
button_sub = Button(cal, text='-', width=10, command=press_sub)
button_sub.grid(row=4, column=4)
# End button
button_end = Button(cal, text='=', width=10, command=press_end)
button_end.grid(row=5, column=4)
# mul button
button_mul = Button(cal, text='*', width=10, command=press_mul)
button_mul.grid(row=1, column=4)
# div button
button_div = Button(cal, text='/', width=10, command=press_div)
button_div.grid(row=2, column=4)

# Open brackets
button_bracket_open = Button(cal, text='(', width=10, command=open_brackets)
button_bracket_open.grid(row=1, column=1)
# Close brackets
button_bracket_close = Button(cal, text=')', width=10, command=close_brackets)
button_bracket_close.grid(row=1, column=2)

# Clear
button_clear = Button(cal, text='C', width=10, command=clear)
button_clear.grid(row=1, column=3)


cal.mainloop()
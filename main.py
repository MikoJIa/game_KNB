from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time


root = Tk()
root.title('Камень ножницы Бумага')
root.geometry('600x450')
root.resizable(width=False, height=False)

pc_score = 0
user_score = 0
pc_figure = ''
user_figure = ''


def but_stone():
    global user_figure
    Stone['bg'] = 'light green'
    Stone['fg'] = 'red'
    Scissors['bg'] = 'white'
    Scissors['fg'] = 'black'
    Paper['bg'] = 'white'
    Paper['fg'] = 'black'
    user_figure = 'Камень'
    pc['state'] = 'normal'


def but_scissors():
    global user_figure
    Stone['bg'] = 'white'
    Stone['fg'] = 'black'
    Scissors['bg'] = 'light green'
    Scissors['fg'] = 'red'
    Paper['bg'] = 'white'
    Paper['fg'] = 'black'
    user_figure = 'Ножницы'
    pc['state'] = 'normal'


def but_paper():
    global user_figure
    Stone['bg'] = 'white'
    Stone['fg'] = 'black'
    Scissors['bg'] = 'white'
    Scissors['fg'] = 'black'
    Paper['bg'] = 'light green'
    Paper['fg'] = 'red'
    user_figure = 'Бумага'
    pc['state'] = 'normal'


def but_pc():
    global pc_score, user_score, user_figure, pc_figure
    for _ in range(30):
        choice = random.randint(1, 4)
        if choice == 1:
            pc_figure = 'Камень'
        if choice == 2:
            pc_figure = 'Ножницы'
        if choice == 3:
            pc_figure = 'Бумага'

        row4['text'] = 'Выбор PC - ' + pc_figure
        row4.update()
        time.sleep(0.1)

    if pc_figure == user_figure:
        messagebox.showinfo('Результат', 'Ничья')
    else:
        if pc_figure == 'Камень' and user_figure == 'Ножницы':
            pc_score += 1
            messagebox.showinfo('result', 'PC - Победил!')
        if pc_figure == 'Камень' and user_figure == 'Бумага':
            user_score += 1
            messagebox.showinfo('result', 'Игрок - Победил!')

        if pc_figure == 'Ножницы' and user_figure == 'Камень':
            user_score += 1
            messagebox.showinfo('result', 'Игрок - Победил!')
        if pc_figure == 'Ножницы' and user_figure == 'Бумага':
            pc_score += 1
            messagebox.showinfo('result', 'PC - Победил!')

        if pc_figure == 'Бумага' and user_figure == 'Камень':
            pc_score += 1
            messagebox.showinfo('result', 'PC - Победил!')
        if pc_figure == 'Бумага' and user_figure == 'Ножницы':
            user_score += 1
            messagebox.showinfo('result', 'Игрок - Победил!')

        row5['text'] = 'Кол-во побед игрока - ' + str(user_score)
        row6['text'] = 'Кол-во побед PC - ' + str(pc_score)

    pc['state'] = 'disabled'

row1 = Label(root, text='Камень Ножницы Бумага', font=('Comic Sans MS', 14, 'bold'), foreground='black')
row1.place(x=200, y=30)

row2 = Label(root, text='Выбор игорока', font=('Comic Sans MS', 14, 'bold'), foreground='red')
row2.place(x=250, y=70)

Stone = Button(root, text='Камень', font=('Arial', 14), fg='light green',
               width=10, height=2, bg='black', command=but_stone)
Stone.place(x=100, y=130)

Scissors = Button(root, text='Ножницы', font=('Arial', 14), fg='light green',
                  width=10, height=2, bg='black', command=but_scissors)
Scissors.place(x=250, y=130)

Paper = Button(root, text='Бумага', font=('Arial', 14), fg='light green',
               width=10, height=2, bg='black', command=but_paper)
Paper.place(x=400, y=130)

row3 = Label(root, text='Выбор компьютера', font=('Comic Sans MS', 14, 'bold'), fg='black')
row3.place(x=220, y=200)
pc = Button(root, text='Компьютер', font=('Arial', 14), bg='black', fg='red', width=15, height=2, command=but_pc)
pc['state'] = 'disabled'  # кнопка не активна
pc.place(x=225, y=250)

row4 = Label(root, text='Выбор PC - 0', font=('Comic Sans MS', 14, 'bold'), fg='black')
row4.place(x=240, y=320)

row5 = Label(root, text='Кол-во побед игрока', font=('Comic Sans MS', 14, 'bold'), fg='blue')
row5.place(x=30, y=400)

row6 = Label(root, text='Кол-во побед PC', font=('Comic Sans MS', 14, 'bold'), fg='red')
row6.place(x=390, y=400)

root.mainloop()

from tkinter import *
import random

window = Tk()
window.title("Pokemon")
window.attributes("-fullscreen", True)
window.config(bg="black", pady=10, padx=10)

icon = PhotoImage(file="pokemon.png")
img = PhotoImage(file="pika.png")

window.iconphoto(True, icon)

attempts = 0


def close_window():
    window.destroy()


def pika():
    global attempts
    attempts += 1
    button.destroy()
    canvas.destroy()
    if attempts >= 3 and random_labels != label:
        random_labels.pack()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        canvas2.destroy()
        canvas3.destroy()
        canvas4.destroy()
        canvas5.destroy()
        canvas6.destroy()
        label_lose.pack()
        window.after(1500, close_window)
    if random_labels == label:
        label.pack()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        canvas2.destroy()
        canvas3.destroy()
        canvas4.destroy()
        canvas5.destroy()
        canvas6.destroy()
        label_win.pack()
        window.after(1500, close_window)


def pika2():
    global attempts
    attempts += 1
    button2.destroy()
    canvas2.destroy()
    if attempts >= 3 and random_labels != label2:
        random_labels.pack()
        button.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        canvas.destroy()
        canvas3.destroy()
        canvas4.destroy()
        canvas5.destroy()
        canvas6.destroy()
        label_lose.pack()
        window.after(1500, close_window)
    if random_labels == label2:
        label2.pack()
        button.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        canvas.destroy()
        canvas3.destroy()
        canvas4.destroy()
        canvas5.destroy()
        canvas6.destroy()
        label_win.pack()
        window.after(1500, close_window)


def pika3():
    global attempts
    attempts += 1
    button3.destroy()
    canvas3.destroy()
    if attempts >= 3 and random_labels != label3:
        random_labels.pack()
        button2.destroy()
        button.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        canvas2.destroy()
        canvas.destroy()
        canvas4.destroy()
        canvas5.destroy()
        canvas6.destroy()
        label_lose.pack()
        window.after(1500, close_window)
    if random_labels == label3:
        label3.pack()
        button2.destroy()
        button.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        canvas2.destroy()
        canvas.destroy()
        canvas4.destroy()
        canvas5.destroy()
        canvas6.destroy()
        label_win.pack()
        window.after(1500, close_window)


def pika4():
    global attempts
    attempts += 1
    button4.destroy()
    canvas4.destroy()
    if attempts >= 3 and random_labels != label4:
        random_labels.pack()
        button2.destroy()
        button3.destroy()
        button.destroy()
        button5.destroy()
        button6.destroy()
        canvas2.destroy()
        canvas3.destroy()
        canvas.destroy()
        canvas5.destroy()
        canvas6.destroy()
        label_lose.pack()
        window.after(1500, close_window)
    if random_labels == label4:
        label4.pack()
        button2.destroy()
        button3.destroy()
        button.destroy()
        button5.destroy()
        button6.destroy()
        canvas2.destroy()
        canvas3.destroy()
        canvas.destroy()
        canvas5.destroy()
        canvas6.destroy()
        label_win.pack()
        window.after(1500, close_window)


def pika5():
    global attempts
    attempts += 1
    button5.destroy()
    canvas5.destroy()
    if attempts >= 3 and random_labels != label5:
        random_labels.pack()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button.destroy()
        button6.destroy()
        canvas2.destroy()
        canvas3.destroy()
        canvas4.destroy()
        canvas.destroy()
        canvas6.destroy()
        label_lose.pack()
        window.after(1500, close_window)
    if random_labels == label5:
        label5.pack()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button.destroy()
        button6.destroy()
        canvas2.destroy()
        canvas3.destroy()
        canvas4.destroy()
        canvas.destroy()
        canvas6.destroy()
        label_win.pack()
        window.after(1500, close_window)


def pika6():
    global attempts
    attempts += 1
    button6.destroy()
    canvas6.destroy()
    if attempts >= 3 and random_labels != label6:
        random_labels.pack()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button.destroy()
        canvas2.destroy()
        canvas3.destroy()
        canvas4.destroy()
        canvas5.destroy()
        canvas.destroy()
        label_lose.pack()
        window.after(1500, close_window)
    if random_labels == label6:
        label6.pack()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button.destroy()
        canvas2.destroy()
        canvas3.destroy()
        canvas4.destroy()
        canvas5.destroy()
        canvas.destroy()
        label_win.pack()
        window.after(1500, close_window)


frame = Frame(window, bg="black")
frame2 = Frame(window, bg="black")
frame3 = Frame(window, bg="black")
frame4 = Frame(window, bg="black")
frame5 = Frame(window, bg="black")
frame6 = Frame(window, bg="black")
frame7 = Frame(window, bg="black")

canvas = Canvas(frame, height=300, width=300, bg="black", highlightthickness=0)

canvas.create_arc(0, 0, 300, 300, fill="#ee1515", extent=180, width=10)
canvas.create_arc(0, 0, 300, 300, fill="#f0f0f0", extent=180, start=180, width=10)
canvas.create_oval(114, 114, 186, 186, fill="#f0f0f0", width=10)

canvas2 = Canvas(frame2, height=300, width=300, bg="black", highlightthickness=0)

canvas2.create_arc(0, 0, 300, 300, fill="#ee1515", extent=180, width=10)
canvas2.create_arc(0, 0, 300, 300, fill="#f0f0f0", extent=180, start=180, width=10)
canvas2.create_oval(114, 114, 186, 186, fill="#f0f0f0", width=10)

canvas3 = Canvas(frame3, height=300, width=300, bg="black", highlightthickness=0)

canvas3.create_arc(0, 0, 300, 300, fill="#ee1515", extent=180, width=10)
canvas3.create_arc(0, 0, 300, 300, fill="#f0f0f0", extent=180, start=180, width=10)
canvas3.create_oval(114, 114, 186, 186, fill="#f0f0f0", width=10)

canvas4 = Canvas(frame4, height=300, width=300, bg="black", highlightthickness=0)

canvas4.create_arc(0, 0, 300, 300, fill="#ee1515", extent=180, width=10)
canvas4.create_arc(0, 0, 300, 300, fill="#f0f0f0", extent=180, start=180, width=10)
canvas4.create_oval(114, 114, 186, 186, fill="#f0f0f0", width=10)

canvas5 = Canvas(frame5, height=300, width=300, bg="black", highlightthickness=0)

canvas5.create_arc(0, 0, 300, 300, fill="#ee1515", extent=180, width=10)
canvas5.create_arc(0, 0, 300, 300, fill="#f0f0f0", extent=180, start=180, width=10)
canvas5.create_oval(114, 114, 186, 186, fill="#f0f0f0", width=10)

canvas6 = Canvas(frame6, height=300, width=300, bg="black", highlightthickness=0)

canvas6.create_arc(0, 0, 300, 300, fill="#ee1515", extent=180, width=10)
canvas6.create_arc(0, 0, 300, 300, fill="#f0f0f0", extent=180, start=180, width=10)
canvas6.create_oval(114, 114, 186, 186, fill="#f0f0f0", width=10)

button = Button(frame, text="Pokemon", font=("Courier", 15, "bold"), fg="#ee1515", bg="black",
                activeforeground="#f0f0f0", activebackground="black", command=pika)
button2 = Button(frame2, text="Pokemon", font=("Courier", 15, "bold"), fg="#ee1515", bg="black",
                 activeforeground="#f0f0f0", activebackground="black", command=pika2)
button3 = Button(frame3, text="Pokemon", font=("Courier", 15, "bold"), fg="#ee1515", bg="black",
                 activeforeground="#f0f0f0", activebackground="black", command=pika3)
button4 = Button(frame4, text="Pokemon", font=("Courier", 15, "bold"), fg="#ee1515", bg="black",
                 activeforeground="#f0f0f0", activebackground="black", command=pika4)
button5 = Button(frame5, text="Pokemon", font=("Courier", 15, "bold"), fg="#ee1515", bg="black",
                 activeforeground="#f0f0f0", activebackground="black", command=pika5)
button6 = Button(frame6, text="Pokemon", font=("Courier", 15, "bold"), fg="#ee1515", bg="black",
                 activeforeground="#f0f0f0", activebackground="black", command=pika6)
label = Label(frame, font=("Courier", 20, "bold"), bg="black",
              compound="top", width=285, height=325, image=img, text="Pikachu!", fg="#ffe62d")
label2 = Label(frame2, font=("Courier", 20, "bold"), bg="black",
               compound="top", width=285, height=325, image=img, text="Pikachu!", fg="#ffe62d")
label3 = Label(frame3, font=("Courier", 20, "bold"), bg="black",
               compound="top", width=285, height=325, image=img, text="Pikachu!", fg="#ffe62d")
label4 = Label(frame4, font=("Courier", 20, "bold"), bg="black",
               compound="top", width=285, height=325, image=img, text="Pikachu!", fg="#ffe62d")
label5 = Label(frame5, font=("Courier", 20, "bold"), bg="black",
               compound="top", width=285, height=325, image=img, text="Pikachu!", fg="#ffe62d")
label6 = Label(frame6, font=("Courier", 20, "bold"), bg="black",
               compound="top", width=285, height=325, image=img, text="Pikachu!", fg="#ffe62d")

label_win = Label(frame7, text="You Win!", font=("Courier", 50, "bold"), bg="black", fg="green")
label_lose = Label(frame7, text="Game Over!", font=("Courier", 50, "bold"), bg="black", fg="green")

labels = [label, label2, label3, label4, label5, label6]
random_labels = random.choice(labels)

frame.place(x=610, y=0)
canvas.pack()
button.pack()
frame2.place(x=1220, y=0)
canvas2.pack()
button2.pack()
frame3.place(x=0, y=430)
canvas3.pack()
button3.pack()
frame4.place(x=610, y=430)
canvas4.pack()
button4.pack()
frame5.place(x=0, y=0)
canvas5.pack()
button5.pack()
frame6.place(x=1220, y=430)
canvas6.pack()
button6.pack()
frame7.place(x=600, y=360)
window.mainloop()

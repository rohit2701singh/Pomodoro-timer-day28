from tkinter import *
import math

BLUE = "#A1CCD1"
NAVY = "#26577C"
BEIGE = "#F4F2DE"
BROWN = "#57375D"
YELLOW = "yellow"
GREEN = "green"
RED = "red"
PINK = "#ff3fa4"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = None

window = Tk()
window.title("My Timer")
# window.minsize(width=400, height=500)
window.config(padx=5, pady=40, bg=BLUE)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", font=(FONT_NAME, 60, "bold"), fg=NAVY)
    check_label.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        start_count(long_break_sec)
        timer_label.config(text="Long Break", font=(FONT_NAME, 50, "bold"), fg=RED)
    elif reps % 2 == 0:
        start_count(short_break_sec)
        timer_label.config(text="Short Break", font=(FONT_NAME, 50, "bold"), fg=PINK)
    else:
        start_count(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 55, "bold"), fg=GREEN)


def start_count(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:  # 09 08 00 format
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"0{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, start_count, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        check_label.config(text=marks)


canvas = Canvas(width=480, height=380, bg=BLUE, highlightthickness=0)
timer_image = PhotoImage(file="timer_img.png")
canvas.create_image(240, 190, image=timer_image)
timer_text = canvas.create_text(285, 265, text="00:00", fill=BEIGE, font=(FONT_NAME, 65, "bold"))

canvas.grid(column=1, row=1)

timer_label = Label(pady=10, text="Timer", font=(FONT_NAME, 60, "bold"), bg=BLUE, fg=NAVY)
timer_label.grid(column=1, row=2)


start_button = Button(pady=1, text="start", width=8, background="#aac8a7", fg="black", font=(FONT_NAME, 15, "bold"),
                      bd=2, command=start_timer)
start_button.place(x=35, y=240)

reset_button = Button(pady=1, text="reset", background="#b9b4c7", fg="black", font=(FONT_NAME, 15, "bold"),
                      width=8, bd=2, command=reset_timer)
reset_button.place(x=35, y=286)

check_label = Label(text="", fg=GREEN, bg=BLUE)
check_label.grid(row=0, column=1)

window.mainloop()

from tkinter import *
import math

# ------------------- CONSTANTS ---------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2
reps = 0
timer = None


# -------------------- TIMER RESET -------------------
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ------------------ TIMER MECHANISM ------------------
def start_timer():
    # count_down(5*60)  # convert min into sec.
    global reps  # (25, 5, 25, 5, 25, 5,25, 20)
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long\nBreak", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short\nBreak", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ----------------- COUNTDOWN MECHANISM ----------------

def count_down(count):
    # count_min = math.floor(count / 60)  # 3.65 = 3
    # count_sec = count % 60
    # print(count_min, count_sec)

    count_min, count_sec = divmod(count, 60)    # divmod() returns a tuple containing the quotient and the remainder

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # .after(delay_millisecond, func, *args), schedule a function to be called after a specified amount of time
        timer = window.after(1000, count_down, count - 1)   # 1000 milliseconds, equivalent to 1 second
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔️"
        check_label.config(text=marks)


# -------------------- UI SETUP -------------------

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(102, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(pady=20, text="Timer", fg=GREEN, font=(FONT_NAME, 45, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", width=10, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

check_label = Label(text="", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

reset_button = Button(text="reset", width=10, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()

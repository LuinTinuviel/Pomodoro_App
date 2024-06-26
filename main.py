from tkinter import *
from tkinter import messagebox
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    done_label.config(text="")

    global reps
    reps = 0

def pause_timer():
    window.after_cancel(timer)
    messagebox.showinfo(title="Info", message="Time to change")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 2 == 1:  # odd reps
        count_down(work_seconds)
        title_label.config(text="Work", fg=GREEN)
    elif reps == 8:  # long break
        count_down(long_break_seconds)
        title_label.config(text="Break", fg=RED)
    else:  # short break
        count_down(short_break_seconds)
        title_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        pause_timer()
        start_timer()

        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in range(work_sessions):
            marks += "✔"
        done_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.rowconfigure(4)
window.columnconfigure(3)

# Timer label
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

# Tomato and counter
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# done label
done_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
done_label.grid(column=1, row=3)

# button Start
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

# button Reset
reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()

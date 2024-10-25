import tkinter as tk
import csv
import random

words_list = []
enter_list = []
correct_chars = 0
timer_started = False
time = 60
current_words = []
word_count = 0
timer_id = None

window = tk.Tk()
window.title("Typing Speed Test App")
window.config(padx=50, pady=50, bg="white")
window.geometry("800x600")


def load_words():
    global words_list
    with open("english_words.csv", newline="") as file:
        words = csv.reader(file)
        words_list = [row[0] for row in words]
        words_list = random.sample(words_list, k=len(words_list))


def start_countdown(event=None):
    global timer_started
    if not timer_started:
        timer_started = True
        countdown(time)


def countdown(count):
    global timer_id
    timer["text"] = count
    if count > 0:
        timer_id = window.after(1000, countdown, count-1)
    else:
        show_result()


def show_result():
    global correct_chars
    popup = tk.Toplevel(window)
    popup.title("Results")
    popup.geometry("400x400")
    result_label = tk.Label(popup, text=f"Your score: {correct_chars}", font=("Arial", 20))
    result_label.pack(pady=20)


def display_words():
    global words_list, current_words
    canvas.delete("all")
    current_words = words_list[:9]
    for i, word in enumerate(current_words):
        row = i // 3
        col = i % 3
        canvas.create_text(100 + col*200, 50 + row*50, text=word, font=("Arial", 20))


def check_word(event=None):
    global enter_list, correct_chars, current_words, word_count, words_list
    typed_word = entry.get().strip()
    if typed_word in current_words:
        correct_chars += len(typed_word)
    enter_list.append(typed_word)
    entry.delete(0, tk.END)
    word_count += 1

    if word_count == 3:
        words_list = words_list[3:]
        display_words()
        word_count = 0


def restart():
    global timer_started, correct_chars, enter_list, current_words, word_count, timer_id
    timer_started = False
    correct_chars = 0
    enter_list = []
    word_count = 0

    load_words()
    if timer_id:
        window.after_cancel(timer_id)
    timer["text"] = time
    display_words()
    entry.delete(0, tk.END)


load_words()

restart_button = tk.Button(window, text="Restart", command=restart)
restart_button.grid(column=2, row=0, pady=20)

timer = tk.Label(window,text=time, bg="white", font=("Courier", 15, "bold"))
timer.grid(column=1, row=0)

canvas = tk.Canvas(window, bg="white", width=600, height=200)
canvas.grid(column=1, row=1, columnspan=2, padx=50, pady=50)

entry = tk.Entry(window, bg="#F8F8FF", width=27, font="Helvetica 20 bold", justify="center")
entry.grid(column=1, row=2, columnspan=2, pady=20)
entry.bind("<KeyPress>", start_countdown)
entry.bind("<space>", check_word)

display_words()

window.mainloop()

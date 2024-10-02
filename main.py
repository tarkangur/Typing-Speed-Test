import tkinter as tk


enter_list = []


window = tk.Tk()
window.title("Typing Speed Test App")
window.config(padx=50, pady=50, bg="white")
window.geometry("800x600")


def countdown(count):
    timer["text"] = count

    if count > 0:
        window.after(1000, countdown, count-1)

    else:
        popup = tk.Toplevel()
        popup.title("Result")


restart_button = tk.Button(window, text="Restart")
restart_button.grid(column=2, row=0, pady=20)

timer = tk.Label(window, bg="white", font=("Courier", 15, "bold"))
timer.grid(column=1, row=0)

canvas = tk.Canvas(window, bg="white", width=400, height=300)
canvas.grid(column=1, row=1, columnspan=2, padx=145)

entry = tk.Entry(window, bg="#F8F8FF", width=27, font="Helvetica 20 bold", justify="center")
entry.grid(column=1, row=2, columnspan=2, pady=20)

countdown(60)


window.mainloop()

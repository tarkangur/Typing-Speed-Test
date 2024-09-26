import tkinter as tk


window = tk.Tk()
window.title("Typing Speed Test App")
window.config(padx=50, pady=50, bg="white")
window.geometry("800x600")


restart_button = tk.Button(window, text="Restart")
restart_button.pack(side=tk.TOP, anchor=tk.E, pady=20)

canvas = tk.Canvas(window, bg="white", width=400, height=300)
canvas.pack()

entry = tk.Entry(window, bg="#F8F8FF", width=70)
entry.pack(pady=20)




window.mainloop()

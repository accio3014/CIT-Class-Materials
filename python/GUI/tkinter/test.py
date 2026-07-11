import tkinter as tk

root = tk.Tk()

def show_value():
    label.config(text="선택한 수량: " + spinbox.get())

root.title("Spinbox 예제")

spinbox = tk.Spinbox(root, from_=1, to=10, width=10, command=show_value)
spinbox.pack(padx=10, pady=10)

label = tk.Label(root, text="선택한 수량: 1")
label.pack(pady=10)

root.mainloop()
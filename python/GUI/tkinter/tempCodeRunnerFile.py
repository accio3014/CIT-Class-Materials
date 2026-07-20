# spinbox_scal.py

import tkinter as tk

root = tk.Tk()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def show_value():
    label.config(text="선택한 수량: " + spinbox.get())

root.title("Spinbox 예제")

spinbox = tk.Spinbox(root, from_=1, to=10, width=10)
spinbox.pack(padx=10, pady=10)

button = tk.Button(root, text="확인", command=show_value)
button.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=10)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


root.mainloop()

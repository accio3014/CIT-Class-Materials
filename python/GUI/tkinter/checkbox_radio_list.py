import tkinter as tk

# def show_result():
#     print(agree_var.get())
#     if agree_var.get():
#         label.config(text="동의했습니다.")

# root = tk.Tk()
# agree_var = tk.BooleanVar()

# check = tk.Checkbutton(root, text="동의합니다", variable=agree_var, command=show_result, state="disabled")
# check.pack(padx=20, pady=20)

# label = tk.Label(root, text="")
# label.pack(pady=10)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


root = tk.Tk()

food = tk.IntVar(value=1)

tk.Radiobutton(root, text="육고기", variable=food, value=1).pack()
tk.Radiobutton(root, text="해산물", variable=food, value=2).pack()



root.mainloop()

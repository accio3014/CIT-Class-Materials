import tkinter as tk

root = tk.Tk()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def show_result():
#     print(agree_var.get())
#     if agree_var.get():
#         label.config(text="동의했습니다.")

# agree_var = tk.BooleanVar()

# check = tk.Checkbutton(root, text="동의합니다", variable=agree_var, command=show_result, state="disabled")
# check.pack(padx=20, pady=20)

# label = tk.Label(root, text="")
# label.pack(pady=10)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# food = tk.IntVar(value=1)

# tk.Radiobutton(root, text="육고기", variable=food, value=1).pack()
# tk.Radiobutton(root, text="해산물", variable=food, value=2).pack()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def show_selected(event):
#     label.config(text="선택한 항목: " + listbox.get(listbox.curselection()))

# listbox = tk.Listbox(root, height=5)
# listbox.pack(padx=10, pady=10)

# for item in ["Python", "Java", "JavaScript", "C", "C++"]:
#     listbox.insert(tk.END, item)

# listbox.bind("<<ListboxSelect>>", show_selected)

# label = tk.Label(root, text="")
# label.pack(pady=10)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


root.mainloop()

import tkinter as tk

def lock_choice():
    selected = food.get()

    for value, radio in radio_buttons:
        if value != selected:
            radio.config(state="disabled")

    label.config(text=f"{selected}번 메뉴를 선택했습니다.")

def reset_choice():
    food.set(0)

    for value, radio in radio_buttons:
        radio.config(state="normal")

    label.config(text="다시 선택할 수 있습니다.")

root = tk.Tk()
root.title("음식 선택")
root.geometry("300x300")

food = tk.IntVar(value=0)

radio_buttons = []

radio1 = tk.Radiobutton(root, text="육고기", variable=food, value=1, command=lock_choice)
radio1.pack(anchor="w", padx=30, pady=5)
radio_buttons.append((1, radio1))

radio2 = tk.Radiobutton(root, text="해산물", variable=food, value=2, command=lock_choice)
radio2.pack(anchor="w", padx=30, pady=5)
radio_buttons.append((2, radio2))

radio3 = tk.Radiobutton(root, text="채소", variable=food, value=3, command=lock_choice)
radio3.pack(anchor="w", padx=30, pady=5)
radio_buttons.append((3, radio3))

radio4 = tk.Radiobutton(root, text="과일", variable=food, value=4, command=lock_choice)
radio4.pack(anchor="w", padx=30, pady=5)
radio_buttons.append((4, radio4))

radio5 = tk.Radiobutton(root, text="디저트", variable=food, value=5, command=lock_choice)
radio5.pack(anchor="w", padx=30, pady=5)
radio_buttons.append((5, radio5))

reset_button = tk.Button(root, text="초기화", command=reset_choice)
reset_button.pack(pady=15)

label = tk.Label(root, text="하나를 선택하세요.")
label.pack(pady=10)

root.mainloop()
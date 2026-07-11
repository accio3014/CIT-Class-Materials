import tkinter as tk

root = tk.Tk()

menubar = tk.Menu(root)                                                 # 1) 메뉴바 생성

file_menu = tk.Menu(menubar, tearoff=0)                                 # 2) 하위 메뉴 생성
file_menu.add_command(label="열기", command=lambda: print("열기 클릭"))     # 3) 항목 채우기
file_menu.add_separator()
file_menu.add_command(label="종료", command=root.destroy)

menubar.add_cascade(label="파일", menu=file_menu)                         # 4) 메뉴바에 연결

root.config(menu=menubar)                                               # 5) 창에 부착
root.mainloop()

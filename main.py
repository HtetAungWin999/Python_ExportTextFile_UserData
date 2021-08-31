import tkinter as tk
from hello_dialog import open_dialog

def main():
    root = tk.Tk()
    button = tk.Button(root, text="Start!", command=open_dialog)
    button.pack(root)

    root.mainloop()
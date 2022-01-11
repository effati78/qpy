import tkinter as tk
root = tk.Tk()
past = 1
def fix(n):
    global past
    n = int(n)
    if not n % 2:
        scale.set(n+1 if n > past else n-1)
        past = scale.get()
scale = tk.Scale(from_=1, to_=99, command=fix, orient=tk.HORIZONTAL)
scale.grid()
root.mainloop()
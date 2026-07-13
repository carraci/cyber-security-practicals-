import tkinter as tk
from tkinter import messagebox

def rail(t, k, d=False):
    if k < 2: return t

    if not d:  
        r = [''] * k
        i, step = 0, 1
        for ch in t:
            r[i] += ch
            i += step
            if i in (0, k - 1):
                step *= -1
        return ''.join(r)

    p = [[] for _ in range(k)]
    i, step = 0, 1
    for j in range(len(t)):
        p[i].append(j)
        i += step
        if i in (0, k - 1):
            step *= -1

    res = [''] * len(t)
    idx = 0
    for row in p:
        for pos in row:
            res[pos] = t[idx]
            idx += 1
    return ''.join(res)


def col(t, k, d=False):
    if len(k) < 2: return t

    n = len(k)
    order = sorted(range(n), key=lambda i: k[i])

    if not d:  # Encrypt
        cols = [''] * n
        for i, ch in enumerate(t):
            cols[i % n] += ch
        return ''.join(cols[i] for i in order)

    
    l = len(t)
    size = [l // n + (i < l % n) for i in range(n)]
    cols, idx = {}, 0

    for i in order:
        cols[i] = t[idx:idx + size[i]]
        idx += size[i]

    return ''.join(
        cols[j][i]
        for i in range(max(size))
        for j in range(n)
        if i < len(cols[j])
    )


def process(mode):
    msg = entry_msg.get()
    key = entry_key.get()
    method = choice.get()

    if not msg:
        messagebox.showerror("Error", "Enter message")
        return

    try:
        if method == "Rail Fence":
            k = int(key)
            if k < 2:
                messagebox.showerror("Error", "Rails ≥ 2")
                return
            out = rail(msg, k, mode == "Dec")

        else:
            if len(key) < 2:
                messagebox.showerror("Error", "Key length ≥ 2")
                return
            out = col(msg, key, mode == "Dec")

        result.set(out)

    except:
        messagebox.showerror("Error", "Invalid input")


root = tk.Tk()
root.title("Cipher Tool")
root.geometry("350x220")

tk.Label(root, text="Message").pack()
entry_msg = tk.Entry(root, width=35)
entry_msg.pack()

tk.Label(root, text="Key / Rails").pack()
entry_key = tk.Entry(root, width=35)
entry_key.pack()

choice = tk.StringVar(value="Rail Fence")
tk.OptionMenu(root, choice, "Rail Fence", "Columnar").pack(pady=5)

tk.Button(root, text="Encrypt", width=15, command=lambda: process("Enc")).pack(pady=2)
tk.Button(root, text="Decrypt", width=15, command=lambda: process("Dec")).pack(pady=2)

result = tk.StringVar()
tk.Label(root, text="Result").pack()
tk.Entry(root, textvariable=result, width=35).pack()

root.mainloop()

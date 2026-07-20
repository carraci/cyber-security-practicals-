import tkinter as tk
from tkinter import messagebox
from math import gcd

# ---------- RSA LOGIC ----------
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = next(e for e in range(2, phi) if gcd(e, phi) == 1)
    d = pow(e, -1, phi)

    return e, d, n

def rsa_process(p, q, data, mode):
    e, d, n = generate_keys(p, q)

    if mode == "Number":
        data = int(data)
        enc = pow(data, e, n)
        dec = pow(enc, d, n)

    else:  # Text
        enc = [pow(ord(ch), e, n) for ch in data]
        dec = "".join(chr(pow(x, d, n)) for x in enc)

    return e, d, n, enc, dec


# ---------- GUI ----------
def process():
    try:
        p, q = int(entry_p.get()), int(entry_q.get())
        data = entry_data.get()
        mode = mode_var.get()

        e, d, n, enc, dec = rsa_process(p, q, data, mode)

        output.set(
            f"Public Key : ({e}, {n})\n"
            f"Private Key: ({d}, {n})\n"
            f"Encrypted  : {enc}\n"
            f"Decrypted  : {dec}"
        )

    except Exception:
        messagebox.showerror("Error", "Invalid input")


# ---------- WINDOW ----------
root = tk.Tk()
root.title("RSA GUI")
root.geometry("380x350")
root.resizable(False, False)

# Title
tk.Label(root, text="RSA Encryption", font=("Arial", 14, "bold")).pack(pady=10)

# Inputs
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="p:").grid(row=0, column=0)
entry_p = tk.Entry(frame, width=10)
entry_p.grid(row=0, column=1)

tk.Label(frame, text="q:").grid(row=1, column=0)
entry_q = tk.Entry(frame, width=10)
entry_q.grid(row=1, column=1)

tk.Label(frame, text="Input:").grid(row=2, column=0)
entry_data = tk.Entry(frame, width=20)
entry_data.grid(row=2, column=1)

# Mode
mode_var = tk.StringVar(value="Number")
tk.OptionMenu(root, mode_var, "Number", "Text").pack(pady=5)

# Button
tk.Button(root, text="Run", command=process, bg="black", fg="white", width=15).pack(pady=10)

# Output
output = tk.StringVar()
tk.Label(root, textvariable=output, bg="#eee", width=45, height=8, justify="left").pack(pady=10)

# Run
root.mainloop()

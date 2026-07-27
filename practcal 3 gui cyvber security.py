import tkinter as tk
from tkinter import messagebox
import hmac
import hashlib

# Function to generate MAC
def generate_mac():
    key = entry_key.get().encode()
    message = entry_message.get().encode()

    if not key or not message:
        messagebox.showerror("Error", "Please enter both key and message")
        return

    mac = hmac.new(key, message, hashlib.sha256).hexdigest()
    entry_mac.delete(0, tk.END)
    entry_mac.insert(0, mac)

# Function to verify MAC
def verify_mac():
    key = entry_key.get().encode()
    message = entry_verify_message.get().encode()
    mac_original = entry_mac.get()

    if not key or not message or not mac_original:
        messagebox.showerror("Error", "Please fill all fields")
        return

    new_mac = hmac.new(key, message, hashlib.sha256).hexdigest()

    if hmac.compare_digest(mac_original, new_mac):
        messagebox.showinfo("Result", "✅ Authentication Successful!\nMessage Integrity Verified.")
    else:
        messagebox.showerror("Result", "❌ Authentication Failed!\nMessage has been modified.")

# GUI Window
root = tk.Tk()
root.title("MAC Generator & Verifier")
root.geometry("500x400")

# Labels & Entries
tk.Label(root, text="Secret Key").pack()
entry_key = tk.Entry(root, width=50)
entry_key.pack()

tk.Label(root, text="Message (Generate MAC)").pack()
entry_message = tk.Entry(root, width=50)
entry_message.pack()

tk.Button(root, text="Generate MAC", command=generate_mac, bg="lightblue").pack(pady=5)

tk.Label(root, text="Generated MAC").pack()
entry_mac = tk.Entry(root, width=50)
entry_mac.pack()

tk.Label(root, text="Message (Verify)").pack()
entry_verify_message = tk.Entry(root, width=50)
entry_verify_message.pack()

tk.Button(root, text="Verify MAC", command=verify_mac, bg="lightgreen").pack(pady=10)

# Run GUI
root.mainloop()

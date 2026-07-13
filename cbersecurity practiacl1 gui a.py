import tkinter as tk

c=lambda t,s:"".join(chr((ord(x)-(65 if x.isupper() else 97)+s)%26+(65 if x.isupper() else 97)) if x.isalpha() else x for x in t)
m=lambda t,k,d=0:"".join((({k[i]:chr(i+97) for i in range(26)} if d else k)[x.lower()].upper() if x.isupper() else ({k[i]:chr(i+97) for i in range(26)} if d else k)[x.lower()]) if x.isalpha() else x for x in t)

def run():
    t=text.get()
    if mode.get()=="Caesar":
        s=int(key.get())
        e=c(t,s)
        out.set(f"Enc: {e}\nDec: {c(e,-s)}")
    else:
        k=key.get()
        e=m(t,k)
        out.set(f"Enc: {e}\nDec: {m(e,k,1)}")

root=tk.Tk()
root.title("Cipher")

mode=tk.StringVar(value="Caesar")
key=tk.StringVar()
text=tk.StringVar()
out=tk.StringVar()

tk.Entry(root,textvariable=mode).pack()
tk.Entry(root,textvariable=key).pack()
tk.Entry(root,textvariable=text).pack()
tk.Button(root,text="Run",command=run).pack()
tk.Label(root,textvariable=out).pack()

root.mainloop()

c=lambda t,s:"".join(chr((ord(x)-(65 if x.isupper() else 97)+s)%26+(65 if x.isupper() else 97)) if x.isalpha() else x for x in t)

m=lambda t,k,d=0:"".join((({k[i]:chr(i+97) for i in range(26)} if d else k)[x.lower()].upper() if x.isupper() else ({k[i]:chr(i+97) for i in range(26)} if d else k)[x.lower()]) if x.isalpha() else x for x in t)

t=input("Msg: ")
ch=input("1.C 2.M: ")

if ch=="1":
    s=int(input("Shift: "))
    e=c(t,s)
    print("Enc:", e)
    print("Dec:", c(e,-s))

else:
    k=input("Key: ")
    e=m(t,k)
    print("Enc:", e)
    print("Dec:", m(e,k,1))

def rail(t, k, d=False):
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


msg = input("Msg: ")

print("1. Rail Fence\n2. Columnar")
ch = input("Choose: ")

if ch == "1":
    k = int(input("Rails: "))
    e = rail(msg, k)
    print("Enc:", e)
    print("Dec:", rail(e, k, True))

elif ch == "2":
    key = input("Key: ")
    e = col(msg, key)
    print("Enc:", e)
    print("Dec:", col(e, key, True))

else:
    print("Invalid choice")

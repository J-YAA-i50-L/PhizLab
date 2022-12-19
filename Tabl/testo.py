import sys


text = list(map(str.strip, sys.stdin))
n, r, g = int(text[0]), list(map(lambda x: int(x), text[1].split(' '))), list(map(lambda x: int(x), text[2].split(' ')))
r.insert(g[0] - 1, g[1])
res = []
if g[0] != 0 and g[0] != len(r) - 1:
    if g[0] - 1 >= 0:
        if r[g[0] - 1] == g[1]:
            k = g[0] - 1
            res1 = []
            if k - 1 >= 0:
                while k - 1 >= 0 and r[k - 1] == g[1]:
                    if r[k - 1] == g[1]:
                        res1.append(r[k - 1])
                        k -= 1
                res += res1
if g[0] + 1 <= len(r) - 1:
    if r[g[0] + 1] == g[1]:
        k = g[0]
        res2 = []
        while k + 1 <= len(r) and r[k + 1] == g[1]:
            if r[k + 1] == g[1]:
                res2.append(r[k + 1])
                k += 1
        res += res2
print(res)

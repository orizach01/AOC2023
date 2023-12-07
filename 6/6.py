def x(a, y):
    return (y + a ** 2) / a


mul = 1
for y in (7, 15, 30):
    for d in (9, 40, 200, 80):
        c = 0
        for a in range(1, d + 1):
            if x(a, y) < d:
                c += 1

mul = 1
ys = (298118510661181,)
cs = (49787980,)

for y, d in zip(ys, cs):
    c = 0
    for a in range(1, d + 1):
        if x(a, y) < d:
            c += 1

    mul *= c

print(mul)

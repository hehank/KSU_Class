a = []
b = 0
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if (i != k) and (i != j) and (j != k):
                b = i*100+j*10+k
                a.append(b)
c = sum(a)
print(c)

def func(x):
    if x % 2 == 0 :
        return "even"
    else :
        return "odd"

l1 = [25,11,12,36,21,52,36,10]

# n1 = list(map(func, l1))
# print(n1)

d = {}

for i in l1 :
    d[i] ="even" if i % 2 == 0 else "odd"
    # d[i] = func(i)

print(d)

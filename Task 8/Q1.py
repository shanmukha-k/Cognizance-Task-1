n1 = int(input("First number: "))
n2 = int(input("Last number: "))
n = n1
o = []
while n <= n2:
    o = o + [n]
    if n != n2:
        o = o + [0]*5
    n = n + 1
print(o)

a = []
b = []
n = int(input("Enter the length of array: "))
print("Start entering the values for first array")
for i in range(n):
    num = int(input())
    a += [num]
print("Start entering the values for second array")
for i in range(n):
    num = int(input())
    b += [num]
print(f'First Array: ', a)
print(f'Second Array: ', b)
c = 0
for i in range(n):
    if a[i] == b[i]:
        c = 1
    else:
        c = 0
if c == 1:
    print("True\nBoth arrays are equal")
elif c == 0:
    print("False\nBoth arrays are not equal")

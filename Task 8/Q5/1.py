import numpy as np

n = int(input("Enter the number of values for an array: "))
a1 = []
i = 0
print("start entering the values for First array")
for i in range(n):
    num = int(input(""))
    a1 += [num]
a2 = []
i = 0
print("start entering the values for Second array")
for i in range(n):
    num = int(input(""))
    a2 += [num]

add = np.add(a1, a2)
print("First array: ", a1)
print("Second array: ", a2)
print("Sum of the arrays is: ", add)
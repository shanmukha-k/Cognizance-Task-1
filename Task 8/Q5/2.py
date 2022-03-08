import numpy as np

print("Enter the size of First matrix(m×n)")
m1 = int(input("m : "))
n1 = int(input("n : "))
print("Enter the size of Second matrix(m×n)")
m2 = int(input("m : "))
n2 = int(input("n : "))
if n1 != m2:
    print("Cant perform multiplication with these sizes :(")
else:
    print("Start entering values for First Matrix: ")
    a = np.random.rand(m1, n1)
    for i in range(m1):
        print('Enter values for row -', i+1, ':')
        for j in range(n1):
            num = int(input(""))
            a[i, j] = num
    print("Start entering values for Second Matrix: ")
    b = np.random.rand(m2, n2)
    for i in range(m2):
        print('Enter values for row -', i + 1, ':')
        for j in range(n2):
            num = int(input(""))
            b[i, j] = num
    print("Your First Matrix is: \n", a)
    print("Your Second Matrix is: \n", b)
    result = np.dot(a, b)
    print("Multiplication result of the matrices is: \n", result)

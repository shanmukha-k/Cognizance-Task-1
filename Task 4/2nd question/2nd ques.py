msg = input("Enter the string: ")
num = (len(msg))
ans = ""
for i in range(0, num):
    if i % 2 == 0:
        ans = ans + msg[i]
print(ans)

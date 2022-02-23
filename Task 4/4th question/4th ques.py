num = input("Enter the number: ")
x = len(num)
org = int(num)
sum = 0
for i in range(0,x):
    a = org%10
    sum = (sum*10)+a
    org = org//10
if int(num)==sum:
    print(f'''TRUE
{num} is a PALINDROME''')
else: print(f'''FALSE
{num} is not a PALINDROME''')
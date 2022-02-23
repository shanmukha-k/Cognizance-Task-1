rows = int(input("Enter number of rows: "))
line = ''
for i in range(1, rows+1):
    line = line + (' '*(rows-1))
    line = line + ('* '*i)
    print(line)
    line = ''
    rows = rows-1

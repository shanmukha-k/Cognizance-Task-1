Table = []
rows = int(input("Enter the number of Students: "))
print("Enter the Roll number, Name and Marks of the student respectively: ")
for row in range(0, rows):
    values = [input(), input(), input()]
    Table.append(values)
print("{:<12}{:<12}{:<12}".format("Roll Number", "Name", "Marks"))
for roll in range(rows):
    for num in range(3):
        print(Table[roll][num], end=" "*10)
    print()
roll = int(input("Enter the Specific Roll Number: "))
print("{:<12}{:<12}{:<12}".format("Roll Number", "Name", "Marks"))
for num in range(3):
    print(Table[roll-1][num], end=" "*10)


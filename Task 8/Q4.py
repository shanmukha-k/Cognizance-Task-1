import pandas as pd

ser = pd.Series(dtype=object)
n = int(input("Enter the number of words: "))
print("Start entering the words: ")
for i in range(n):
    w = pd.Series([input()])
    ser = pd.concat([ser, w], ignore_index=True)
ser = ser.str.title()
print(ser)

line1 = ["[ ]", "[ ]", "[ ]"]
line2 = ["[ ]", "[ ]", "[ ]"]
line3 = ["[ ]", "[ ]", "[ ]"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to put the treasure? A1, B3, C2 etc.\n")
x = position[0]
y = position[1]
x_map_ref = 0
y_map_ref = 0

if x == 'A':
    x_map_ref = 0
elif x == 'B':
    x_map_ref = 1
elif x == 'C':
    x_map_ref = 2

if y == '1':
    y_map_ref = 0
elif y == '2':
    y_map_ref = 1
elif y == '3':
    y_map_ref = 2

map[x_map_ref][y_map_ref] = '[X]'

print(f"{line1}\n{line2}\n{line3}")

student_heights = input("Enter the heights of students (space separated)\n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0

for height in student_heights:
    total_height += height

number_of_students = 0

for student in student_heights:
    number_of_students += 1

avg_height = round(total_height / number_of_students)

print(f"Total height: {total_height}")
print(f"Number of students: {number_of_students}")
print(f"Average student height is: {avg_height}")

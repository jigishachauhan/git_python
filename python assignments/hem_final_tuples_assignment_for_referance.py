students = ("Aarav", "Priya", "Rohan", "Meera", "Kabir", "Isha", "Vikram", "Diya")

#Part A — Tuple Creation & Positive Indexing

print("PART A")
#1. Print the entire students tuple and also print its length using len().
print("Given Tuple is : ", students, " and its length is : ", len(students))

#2. Access and print the first student in the tuple using positive indexing.
print("First student in the tuple : ", students[0])

#3. Access and print the fourth student using positive indexing.
print("Fourth student in the tuple : ", students[3])

#4. Print the first 3 students using slicing.
print("First 3 students in the tuple : ", students[:3])

#5. Print students from index 2 to index 5 (both included) using slicing.
print("Index 2 student to Index 5 student in the tuple : ", students[2:6])

print()
#Part B — Negative Indexing & Slicing
print("PART B")

#6. Access and print the last student ("Diya") using only negative indexing.
print("Last student in the tuple : ", students[-1])

#7. Access and print the second-last student using only negative indexing.
print("Last second student in the tuple : ", students[-2])

#8. Print the last 3 students of the tuple using negative indexing.
print("Last 3 students in the tuple : ", students[-3:])

#9. Print the first student and the last student of the tuple using positive and negative indexing respectively, in the same line.
print("First student in the tuple : ", students[0], ", Last student in the tuple : ", students[-1])
# print(f"This is the F string method : First student in the tuple : {students[0]} Last student in the tuple : {students[-1]}")

#10. Reverse the entire students tuple using slicing.
print("Reverse the tuple : ", students[::-1])

print()
#Part C — Tuple Methods & Immutability
print("PART C")

#11. Use count() to find how many times "Rohan" appears in the tuple.
print("\"Rohan\" appears in the tuple : ", students.count("Rohan"), "time")

#12. Use index() to find the position of "Kabir" in the tuple.
print("Position of \"Kabir\" in the tuple : ", students.index("Kabir"))

#13. Try to change the second element of the tuple to "Ananya", print the error message you get, and explain in a comment why this happens.
try:
    students[1] = "Ananya"
except TypeError as e:
    # Tuples are immutable, meaning their elements cannot be changed, modified, added, or removed after creation.
    print("Changing the Second Element gives an error like : ", e)

#14. Convert the students tuple into a list, add "Ananya" to it, then convert it back into a tuple.
temp_list = list(students)
temp_list.append("Ananya")
students_updated = tuple(temp_list)
print("Tuple after converting to list, adding 'Ananya', and back to tuple : ", students_updated)

#15. Concatenate the students tuple with a new tuple ("Neha", "Arjun") and print the result.
new_students = students + ("Neha", "Arjun")
print("Concatenated tuple : ", new_students)

#16. Repeat the tuple ("Pass", "Fail") 3 times using the * operator and print the result.
repeated_tuple = ("Pass", "Fail") * 3
print("Repeated tuple : ", repeated_tuple)

#17. Use sorted() to print the students in alphabetical order (note that this returns a list, not a tuple — explain why in a comment).
# sorted() always returns a new sorted list because its standard implementation creates and returns a list data structure regardless of the input iterable type.
print("Sorted students in alphabetical order (returns a list) : ", sorted(students))

print()
#Part D — Mixed / Applied
print("PART D")

#18. Given a tuple of marks, marks = (78, 45, 89, 92, 34, 67, 55, 88), write code to:
marks = (78, 45, 89, 92, 34, 67, 55, 88)
# • Print the highest and the lowest marks using max() and min().
print("Highest mark : ", max(marks), "and Lowest mark : ", min(marks))
# • Print the total of all marks using sum().
print("Total of all marks : ", sum(marks))

#19. Create a nested tuple exam_data = (("Aarav", 78), ("Priya", 92), ("Rohan", 45)) and write code to print the names and marks of students using formatting.
exam_data = (("Aarav", 78), ("Priya", 92), ("Rohan", 45))
print("Exam Data Details:")
for name, mark in exam_data:
    print(f"Student Name: {name}, Marks: {mark}")

#20. Use tuple unpacking to assign the values ("Python", "Tuples", 2026) to three variables subject, topic, year in a single line, then print each variable.
subject, topic, year = ("Python", "Tuples", 2026)
print(f"Subject: {subject}, Topic: {topic}, Year: {year}")
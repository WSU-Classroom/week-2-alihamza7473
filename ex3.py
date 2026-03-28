# Ask teacher to enter marks
math = int(input("Enter Math marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))

# Store marks in a list
marks = [math, english, science]

# Calculations
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

# Print results
print("\n----- Student Result Summary -----")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)

math = 80
english = 75
science = 85


scores = [math, english, science]

total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)



print("Student Result Summary")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
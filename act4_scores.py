# Name: Maderazo, Marshal Reign A.
# Section: BAET 2102

students = int(input("Students: "))

scores = []

for i in range(students):
    score = float(input(f"Score {i + 1}: "))
    scores.append(score)

total = sum(scores)
average = total / students
highest = max(scores)

print(f"Total: {total:g}")
print(f"Avg: {average:.2f}")
print(f"Highest: {highest:g}")
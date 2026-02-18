print("Expense Splitter")

people = int(input("Enter number of people: "))

i = 0
total_expense = 0

while i < people:
    expense = int(input("Enter expense: "))
    total_expense = total_expense + expense
    i = i + 1

share = total_expense / people   # ❌ Mistake 1: Division done before checking if people == 0 (may cause ZeroDivisionError)

print("Total Expense:", total_expense)
print("Each Share:", share)

if share < 0:   # ❌ Mistake 2: Unnecessary condition (share normally cannot be negative)
    print("Invalid share")

if people = 0:   # ❌ Mistake 3: Wrong operator (= used instead of ==)
    print("Cannot divide by zero")

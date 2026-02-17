print("Expense Splitter")

people = int(input("Enter number of people: "))

if people == 0:
    print("Cannot divide by zero")
else:
    i = 0
    total_expense = 0

    while i < people:
        expense = int(input("Enter expense: "))
        total_expense = total_expense + expense
        i = i + 1

    share = total_expense / people

    print("Total Expense:", total_expense)
    print("Each Share:", share)
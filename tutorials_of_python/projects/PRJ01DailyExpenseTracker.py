print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense\n2. View all expenses\n3. Calculate total and average expense\n4. Clear all expenses\n5. Exit")

expenses = []

while True:
    choice = input()
    
    if choice == "1":
        expenses.append(float(input()))
        print("Expense added successfully!")

    elif choice == "2":
        if not len(expenses):
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i, v in enumerate(expenses):
                print(f"{i+1}. {v}")
    
    elif choice == "3":
        if not len(expenses):
            print("No expenses recorded yet.")
        else:
            total = sum(expenses)
            number = len(expenses)
            average = round(total/number, 1)
            print(f"Total expense: {total}")
            print(f"Average expense: {average}")

    elif choice == "4":
        expenses.clear()
        print("All expenses cleared.")
        # print(expenses)

    elif choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
"""
Ashanti Evans
Student Budget Tracker
"""

import csv 

print("WELCOME TO THE STUDENT BUDGET TRACKER!" )
print("------------------------------------------")


income=float(input("Enter available money: $"))

# ASK FOR A SPENDING BUDGET
budget_limit = float(input("Enter your monthly spending limit: $"))

#Create list to store expenses
expense_names=[]
expense_amounts=[]

while True:
    name = input("Enter expense name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    amount = float(input("Enter expense amount: $"))
    expense_names.append(name)
    expense_amounts.append(amount)




#calculate total expenses
total_expenses = sum(expense_amounts)
remaining_balance = income - total_expenses

# Calculate remaining budget
budget_remaining = budget_limit - total_expenses




#Ask about savings goal
savings_goal = float(input("What is your savings goal? ($):"))

#The results
print("" + "=" * 40)
print("                         STUDENT BUDGET TRACKER")
print("" + "=" * 40)


print(f"Available money:             ${income:.2f}")
print(f"Total expenses:              ${total_expenses:.2f}")
print(f"Remaining balance:           ${remaining_balance:.2f}")

print("-" * 40)
print(f"Spending budget:             ${budget_limit:.2f}")
print(f"Monthly budget remaining:    ${budget_remaining:.2f}")
print(f"Your savings goal is:        ${savings_goal:.2f}")
print("-" * 40)


#check if the goal has been met
if remaining_balance < 0:
    print("Warning: You spent more than you have!")
else:
    print("You are within your available budget.")

#Check spending budget
if budget_remaining < 0:
    print("BUDGET ALERT: You have exceeded your spending budget!")
elif budget_remaining ==0:
    print("You have reached your spending budget!")
else:
    print(f"You can spend another ${budget_remaining:.2f} within your budget.")

if remaining_balance < 0:
    print("You need to reduce your expenses")
elif remaining_balance >= savings_goal:
    print("Congratulations! You have reached your savings goal.")
else:
    amount_needed = savings_goal - remaining_balance
    print(f"You are on track to reach your savings goal. You need ${amount_needed:.2f} more to reach your goal.")

with open("/Users/ashantievans/Documents/budget_report.csv", "w", newline="") as file:
    writer=csv.writer(file)

    writer.writerow(["Student Budget and Saving Tracker"])
    writer.writerow(["Available Money", f"${income:.2f}"])
    writer.writerow(["Monthly Spending Budget", f"${budget_limit:.2f}"])
    writer.writerow(["Monthly Spending Budget", f"${budget_limit:.2f}"])
    writer.writerow([])
    writer.writerow(["Expense", "Amount"])

    for i in range(len(expense_names)):
        writer.writerow([expense_names[i], f"${expense_amounts[i]:.2f}"])


    writer.writerow(["Total Expenses", f"${total_expenses:.2f}"])
    writer.writerow([f"Remaining Balance", f"${remaining_balance:.2f}"])
    writer.writerow(["Budget Remaining", f"${budget_remaining:.2f}"])
    writer.writerow(["Savings Goal", f"${savings_goal:.2f}"])

print("Your budget report was saved as budget_report.csv")
print("===============================================================================")
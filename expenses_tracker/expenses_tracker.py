menu= """========== EXPENSE TRACKER ==========
1. Add Expense
2. View All Expenses
3. View Total Spending
4. Exit\n\n"""

expenses=[]

while True:
    print(menu)
    
    choice=input("Choose an option:")
    
    if choice == "1":
        amount=int(input("Enter amount: "))
        category=input("Enter category food/entertainement/transport/other : ")

        expenses.append({"amount":amount ,"category":category})
        print("Expense added!")
    
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet!")
        else:
            for expense in expenses:
                print(f"{expense['category']} - ${expense['amount']}")




    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense['amount']
        print(f"Total spending: ${total}")
       

    elif choice == "4":
        print("goodbye!")
        break
    
    else:
        print("Error!")
from datetime import datetime
now = datetime.now()
print("\t--Budget Tracker For Expenses--",now.strftime("%d-%m-%Y %H:%M:%S"))

expense = []

while True:
  print('''\n1. Add Expense.
2. View Expense.
3. Total number of Expenses.
4. Exit.
''')
  
  option = input("Select the option: ")
    
  if option.startswith("1"):
        Expenses = 0
        Expenses = int(input("Add Expense: "))
        Name = input('Enter your name: ')
        expense.append(Name)
        expense.append(Expenses)   
    
  elif option.startswith("2"):
        if expense:
            print(expense)
        else:
            print("No Expenses Exist")

  elif option.startswith("3"):
      total_expenses = len(expense) // 2
      print(f"Total number of Expenses = {total_expenses}")

  elif option.startswith("4"):
      print("Thanks for using our services")
      break
  else:
      print('invalid option')
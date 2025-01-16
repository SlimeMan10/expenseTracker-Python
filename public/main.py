from tracker import tracker

# Constants
totalChoices = 6
object = None  # Global tracker object

# Entry Point
def init():
    print("This is my budget tracker")
    print("1. Load data")
    print("2. Start with new data")
    while True:
        try:
            num = int(input("Option: "))
            if num < 1 or num > 2:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid number (1 or 2)")
            print()
    if num == 1:
        readFile()
    else:
        startNewBudget()

def readFile():
    print("Functionality not implemented yet")

def startNewBudget():
    global object
    print("Starting new budget")
    while True:
        try:
            num = int(input("Enter your budget (must be greater than zero): "))
            if num <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid positive number")
    object = tracker(num)
    start()

def start():
    while True:
        printOptions()
        try:
            choice = int(input("Choice: "))
            if choice < 0 or choice > totalChoices:
                raise ValueError
        except ValueError:
            print("Enter a valid choice")
            print()
            continue
        if choice == 0:
            print("Exiting the tracker. Goodbye!")
            break
        checkOptions(choice)

def checkOptions(choice):
    match choice:
        case 1:
            addExpense()
        case 2:
            removeExpense()
        case 3:
            reviewAll()
        case 4:
            reviewCategory()
        case 5:
            save()
        case 6:
            updateBudget()

def addExpense():
    global object
    category = getCategory()
    name = input("What is the name of the expense? ")
    while True:
        try:
            price = float(input("What is the price of the expense? "))
            if price < 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid price")
    object.add_expense(category, name, price)
    print(f"Added '{name}' (${price}) to category '{category}'.")

def removeExpense():
    global object
    category = getCategory()
    object.printCategory(category)
    size = object.sizeOfCategory(category)
    if (size == 0):
        print("Category is empty")
    else:
        while True:
            try:
                index = int(input("Enter the number of the item to remove: "))
                if index < 1 or index > size:
                    raise ValueError
                break
            except ValueError:
                print("Enter a valid number")
        object.remove_expense(category, index-1)
        print("Expense removed successfully.")

def reviewAll():
    global object
    object.printAll()

def reviewCategory():
    global object
    category = getCategory()
    object.printCategory(category)

def getCategory():
    while True:
        try:
            printCategories()
            item = int(input("Choose a category (1-6): "))
            if item < 1 or item > 6:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid number between 1 and 6")
    match item:
        case 1: return "food"
        case 2: return "transport"
        case 3: return "shopping"
        case 4: return "entertainment"
        case 5: return "travel"
        case 6: return "technology"

def printCategories():
    print("1. Food")
    print("2. Transport")
    print("3. Shopping")
    print("4. Entertainment")
    print("5. Travel")
    print("6. Technology")

def save():
    print("Save functionality is in progress.")

def updateBudget():
    global object
    while True:
        try:
            num = float(input("Enter your new budget (must be greater than zero): "))
            if num <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid positive number")
    object.setNewBudget(num)
    print(f"New budget set to ${num:.2f}")

def printOptions():
    print("Here are your options:")
    print("1. Add purchase")
    print("2. Remove purchase")
    print("3. Review all purchases")
    print("4. Review a specific category")
    print("5. Save current tracker")
    print("6. Change budget")
    print("0. Exit")

# Graceful exit for keyboard interrupt
try:
    init()
except KeyboardInterrupt:
    print("\nTracker exited. Goodbye!")
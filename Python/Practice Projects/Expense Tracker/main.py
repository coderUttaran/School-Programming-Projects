transaction = []
balance = 0

def showbalance():
    global balance
    print(f"\nBalance: {balance}")

def addMoney():
    global balance
    money = float(input("\nEnter amount to add: "))
    print(f"\n{money} is added")
    balance+=money
    print(f"New Balance: {balance}")
    transaction.append(f"+ {money}")

def deductMoney():
    global balance
    money = float(input("\nEnter amount to deduct: "))
    if money > balance:
        print(f"\n{money} can't be debited as the balance is {balance}")
    else:
        print(f"\n{money} is deducted")
        balance-=money
        print(f"\nNew Balance: {balance}")
        transaction.append(f"- {money}")
        

def showTransactions():
    print("\n")
    for i in range(len(transaction)):
        print(f"{i + 1}. {transaction[i]}")

def main():
    while True:
        print("\n----Welcome to Budget Tracker----")
        print("1. Show Balance")
        print("2. Add Money")
        print("3. Deduct Money")
        print("4. Show Transactions")
        print("5. Exit")

        try:
            choice = int(input("\nEnter Operation (1, 2, 3, 4, 5): "))
            if choice in range(1, 6):
                if choice == 1:
                    showbalance()
                elif choice == 2:
                    addMoney()
                elif choice == 3:
                    deductMoney()
                elif choice == 4:
                    showTransactions()
                else:
                    print("\nThank you for using our budget tracker")
                    print("Exiting....")
                    break
            else:
                print("\nInvalid Input\nPlease Choose Betwen 1-5")
        
        except ValueError:
            print("\nInvalid Input")

main()

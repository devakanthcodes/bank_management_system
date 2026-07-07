import json

accounts = []
transactions = []

# ================= LOAD ACCOUNTS =================

def load_accounts():
    global accounts
    try:
        with open("accounts.json", "r") as f:
            accounts = json.load(f)
    except:
        accounts = []

# ================= SAVE ACCOUNTS =================

def save_accounts():
    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)

# ================= LOAD TRANSACTIONS =================

def load_transactions():
    global transactions
    try:
        with open("transactions.json", "r") as f:
            transactions = json.load(f)
    except:
        transactions = []

# ================= SAVE TRANSACTIONS =================

def save_transactions():
    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)

# ================= ADMIN LOGIN =================

def login():
    print("\n===== BANK MANAGEMENT SYSTEM =====")

    password = input("Enter Admin Password: ")

    if password == "admin123":
        print("Login Successful ✅")
    else:
        print("Wrong Password ❌")
        exit()

# ================= CREATE ACCOUNT =================

def create_account():
    account_no = input("Enter Account Number: ")
    name = input("Enter Customer Name: ")
    balance = float(input("Enter Initial Balance: "))

    account = {
        "account_no": account_no,
        "name": name,
        "balance": balance
    }

    accounts.append(account)
    save_accounts()

    print("✅ Account Created Successfully!")

# ================= DEPOSIT MONEY =================

def deposit_money():
    account_no = input("Enter Account Number: ")
    amount = float(input("Enter Deposit Amount: "))

    for account in accounts:
        if account["account_no"] == account_no:
            account["balance"] += amount
            save_accounts()

            transactions.append({
                "account_no": account_no,
                "type": "Deposit",
                "amount": amount
            })
            print(transactions)
            save_transactions()

            print("✅ Money Deposited Successfully!")
            return

    print("❌ Account Not Found!")

# ================= WITHDRAW MONEY =================

def withdraw_money():
    account_no = input("Enter Account Number: ")
    amount = float(input("Enter Withdraw Amount: "))

    for account in accounts:
        if account["account_no"] == account_no:

            if account["balance"] >= amount:
                account["balance"] -= amount
                save_accounts()

                transactions.append({
                    "account_no": account_no,
                    "type": "Withdraw",
                    "amount": amount
                })
                save_transactions()

                print("✅ Money Withdrawn Successfully!")
            else:
                print("❌ Insufficient Balance!")

            return

    print("❌ Account Not Found!")

# ================= CHECK BALANCE =================

def check_balance():
    account_no = input("Enter Account Number: ")

    for account in accounts:
        if account["account_no"] == account_no:
            print("\n===== ACCOUNT DETAILS =====")
            print("Account Number :", account["account_no"])
            print("Customer Name  :", account["name"])
            print("Balance        :", account["balance"])
            return

    print("❌ Account Not Found!")

# ================= CHECK BALANCE =================

# ================= TRANSACTION HISTORY =================

def transaction_history():
    account_no = input("Enter Account Number: ")

    found = False

    print("\n===== TRANSACTION HISTORY =====")

    for transaction in transactions:
        if transaction["account_no"] == account_no:
            print(
                f'{transaction["type"]} : ₹{transaction["amount"]}'
            )
            found = True

    if not found:
        print("No Transactions Found!")

# ================= SEARCH ACCOUNT =================

def search_account():
    account_no = input("Enter Account Number: ")

    for account in accounts:
        if account["account_no"] == account_no:
            print("\n===== ACCOUNT FOUND =====")
            print("Account Number :", account["account_no"])
            print("Customer Name  :", account["name"])
            print("Balance        :", account["balance"])
            return

    print("❌ Account Not Found!")

# ================= DELETE ACCOUNT =================

def delete_account():
    account_no = input("Enter Account Number: ")

    for account in accounts:
        if account["account_no"] == account_no:
            accounts.remove(account)
            save_accounts()
            print("✅ Account Deleted Successfully!")
            return

    print("❌ Account Not Found!")

# ================= MAIN MENU =================

def menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Search Account")
        print("7. Delete Account")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            search_account()
        elif choice == "7":
            delete_account()
        elif choice == "8":
            print("Thank you for using Bank Management System!")
            break
        else:
            print("Invalid Choice!")

load_accounts()
load_transactions()
login()
menu()

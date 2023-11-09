
account_balance = 0
accounts_dict = {
    "Account_A":100000,
    "Account_B":17000,
    "Account_C":560000
}
print("Welcome to your Bank Acccount Manager")

account_request = input ("Would you like to access account A, B, or C? : ")
account_request = account_request.upper()

if account_request not in ["A", "B", "C"]:
    print("You did not enter a valid account letter. Please enter A, B or C: ")
elif account_request == "A":
    account_balance = accounts_dict["Account_A"]
elif account_request == "B":
    account_balance = accounts_dict["Account_B"]
elif account_request == "C":
     account_balance = accounts_dict["Account_C"]

while True:


    user_request = input(
        "Select which action to perform from the following menu:\n"
        "To view your account balance- enter 1\n"
        "To deposit money- enter 2\n"
        "To withdraw money- enter 3\n"
        "To exit the program- enter 4\n"
        "I would like to: "
    )

    if user_request == "4": #Exit the program
        break
    elif user_request not in ["1","2","3","4"]:
        print("You did not enter a valid command, please enter 1, 2, 3, or 4")
    elif user_request == "1": # View account balance
        print("\nAccount balance: " + str(account_balance) + "\n\n")

    elif user_request == "2": # Deposit money
        deposit_amount = input("\nEnter the amount you want to deposit: ")
        account_balance = account_balance + int(deposit_amount)
        print("$" + deposit_amount + " has been added to your account, and your new account balance is $" + str(account_balance) + "\n\n")

    elif user_request == "3": # Withdraw money
        withdraw_amount = input("\nEnter the amount you want to withdraw: ")
        account_balance = account_balance - int(withdraw_amount)
        print("$" + withdraw_amount + " has been withdrawn from your account. Your new account balance is $" + str(account_balance) + "\n\n")

# Question: Can we go through how I would implement this with functions? And why I would use functions here?

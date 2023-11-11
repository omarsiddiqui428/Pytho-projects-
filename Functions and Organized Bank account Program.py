#Global Variables first
accounts_dict = {
    "Account_A":100000,
    "Account_B":17000,
    "Account_C":560000
}

#Functions right under global variables
def deposit(account_request):
    deposit_amount = input("\nEnter the amount you want to deposit: ")
    accounts_dict[account_request] = accounts_dict[account_request] + int(deposit_amount)
    print("$" + deposit_amount + " has been added to your account, and your new account balance is $" + str(accounts_dict[account_request]) + "\n\n")

def withdraw(account_request):
    withdraw_amount = input("\nEnter the amount you want to withdraw: ")
    if accounts_dict[account_request] >= int(withdraw_amount):
        accounts_dict[account_request] = accounts_dict[account_request] - int(withdraw_amount)
        print("$" + withdraw_amount + " has been withdrawn from your account. Your new account balance is $" + str(
            accounts_dict[account_request]) + "\n\n")
    else:
        print("You do not have " + str(
            withdraw_amount) + " available to withdraw. The max you can withdraw from this account is " + str(
            accounts_dict[account_request]) + ".\n\n")
def main(): #last function should always be main method

    print("Welcome to your Bank Acccount Manager")
    account_request = input ("Would you like to access account A, B, or C? : ")
    account_request = account_request.upper()

    if account_request not in ["A", "B", "C"]:
        print("You did not enter a valid account letter. Please enter A, B or C: ")

    account_request = "Account_" + account_request

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
            print("\nAccount balance: " + str(accounts_dict[account_request]) + "\n\n")

        elif user_request == "2": # Deposit money
            deposit(account_request)

        elif user_request == "3": # Withdraw money
            withdraw(account_request)

#last thing in program (specific to python for this syntax), you have to call the main function
if __name__ == "__main__": #put this in whatever file has the main logic of your code
    main()
print("Simple Bank Transfer System")
real_user_id = "1234"
real_balance = 2452.21
valid_account_number = "98765"
user_id = input("Enter your user ID: ")

if user_id != real_user_id:
    print("Unknown user ID")
else:
    # The user ID is valid
    # read amount to transfer
    amount_to_transfer = float(input("How much do you want to transfer: "))
    recipient_account_number = input("Enter the account number: ")

    # Amount to transfer must not be negative
    if amount_to_transfer <= 0:
        print("Invalid amount:", amount_to_transfer)
    else:
        # The charges amount to a total of 1 percent of the amount to be transferred
        charges = 0.01 * amount_to_transfer
        total_amount_to_be_deducted = amount_to_transfer + charges

        print("Applicable charges:", charges)
        print("Total debit amount:", total_amount_to_be_deducted)

        # The balance must contain at least the amount to transfer plus charges
        if real_balance < total_amount_to_be_deducted:
            print("Insufficient funds")
        else:
            # The account number must be valid:
            if recipient_account_number != valid_account_number:
                print("Invalid account number:", recipient_account_number)
            else:
                print("Transfer successful")
                real_balance -= total_amount_to_be_deducted
                print(f"Current balance: {real_balance:.2f}")
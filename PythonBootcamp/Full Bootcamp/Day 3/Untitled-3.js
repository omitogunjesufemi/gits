var username = "Omitogun Jesufemi";
var initial_account_balance = 100000;
var amount_to_be_withdrawn = 1000000;
var after_withdrawal_account_balance = initial_account_balance - amount_to_be_withdrawn;

// Access to overdraft boolean check.
if ((after_withdrawal_account_balance < 0)) {
    overdraft_access = true;
    console.log(overdraft_access);
} else {
    overdraft_access = false;
    console.log(overdraft_access);
}

// Checking if amount to be withdrawn is below the initial balance.
if (amount_to_be_withdrawn <= initial_account_balance) {
    message = `Dear ${username}, Your withdrawal of N ${amount_to_be_withdrawn} was successful!`;
    console.log(message);
}

// Checking if amount to be withdrawn is above the initial balance.
if ((amount_to_be_withdrawn > initial_account_balance) && (overdraft_access == true)) {
    message = `Dear ${username}, Your withdrawal of N ${amount_to_be_withdrawn} was successful with an overdraft!`;
    console.log(message);
}
else {
    message = `Dear ${username}, Your withdrawal of N ${amount_to_be_withdrawn} was unsuccessful!`;
    console.log(message);
}
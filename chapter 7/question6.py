def check_account_validity(user_input, valid_accounts):
    if user_input in valid_accounts:
        return "Valid account number."
    else:
        return "Invalid account number."
with open('charge_accounts.txt', 'r') as file:
    valid_accounts = [line.strip() for line in file]
    user_input = input("Enter a charge account number: ")
result = check_account_validity(user_input, valid_accounts)
print(result)
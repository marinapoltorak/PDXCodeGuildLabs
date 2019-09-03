class ATM:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transaction_list = []

    def __str__(self):
        return f'ATM\n Balance: {self.balance}\n Interest rate:'

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_list.append(f'user deposited {amount}')
        return self.balance

    def check_withdrawal(self, amount):
        return self.balance > amount

    def withdraw(self, amount):
        self.transaction_list.append(f'user withdrew {amount}')
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        pass

    def print_transaction(self):
        for transaction in self.transaction_list:
            return transaction
            print(transaction)

an_atm = ATM(0,0.1)
while True:
    x = input('what would you like to do (deposit, withdraw, balance or history)?: ')
    if x == 'deposit':
        y = int(input('how much would you like to deposit?: '))
        an_atm.deposit(y)
    elif x == 
print(an_atm.check_balance())

# user_choice = input('what would you like to do (deposit, withdraw, balance or history)?: ')
# if user_choice == 'deposit':
#     deposit = float(input('how much would you like to deposit?: '))
#     print(f' d: {deposit}')
# elif user_choice == 'withdraw':
#     withdraw = float(input('how much would you like to withdraw?: '))
#     print(f' w: {withdraw}')
# elif user_choice == 'balance':
#     print(self.balance)
# else:
#     print(print_transaction())
#
# an_atm = ATM(0, 0.1)
#
# print(an_atm.check_balance())
# print(an_atm.print_transaction())
# an_atm.deposit(deposit)
# an_atm.withdraw(withdraw)
# print(an_atm)
# an_atm.print_transaction()

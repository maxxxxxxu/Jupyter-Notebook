from datetime import datetime

class Account:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount: float):
       if amount > 0:
            self.balance += amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append(f'{timestamp}: На баланс аккаунта {self.name} добавлено {amount}')
        
    def withdrawal(self, amount: float):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if amount > 0: 
            if amount < self.balance:
                self.balance -= amount
                self.history.append(f'{timestamp}: С аккаунта {self.name} снято {amount}')
            else:
                self.history.append(f'{timestamp}: Попытка снятия средств с аккаунта {self.name}, больше чем есть на балансе')

    def print_balance(self):
        print(f'Баланс аккаунта {self.name}: {self.balance}')

    def operation_history(self):
        print(self.history)


#Создаем счета
igor_wallet = Account(name="Igor", balance=200)
maksim_wallet = Account(name="Maksim", balance=200000)

#Операции по счетам
igor_wallet.deposit(100)
maksim_wallet.withdrawal(2000)
igor_wallet.withdrawal(100)
igor_wallet.withdrawal(100)
maksim_wallet.withdrawal(21000)
igor_wallet.withdrawal(10000)
maksim_wallet.withdrawal(2000)

#Проверяем баланс счетов
igor_wallet.print_balance()
maksim_wallet.print_balance()

#Смотрим историю операций по счетам
igor_wallet.operation_history()
maksim_wallet.operation_history()
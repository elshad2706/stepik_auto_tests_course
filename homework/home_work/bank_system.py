class BankAccount:
    def __init__(self, name, balance):  # аргумент конструктора
        self.name = name
        self.balance = balance  # Атрибут объекта

    def replenishment(self,
                      amount):  # self в качестве первого аргумента, что является обязательным для методов экземпляра класса.
        try:
            if amount > 0:
                self.balance += amount
                print(f'Ваши деньги в размере {amount} рублей внесены на счёт')
                print(f'Обновленный баланс {self.balance} рублей')
            elif amount <= 0:
                print(f'Сумма {amount} меньше допустимой')
        except AssertionError:
            print('Ошибка при пополнении баланса')

    def withdraw(self, amount):
        if amount > self.balance:
            print('На счете не достаточно средств')
        elif amount < self.balance or amount == self.balance:
            after_withdraw = self.balance - amount
            print(f'Выведено с баланса {amount} рублей')
            print(f'Остаток на балансе {after_withdraw} рублей')

    def transwer(self, amount, target_account):
        if amount > self.balance:
            print(f'Не доступно для перевода,так как ваш баланс ={balance} больше чем сумма перевода')
        elif amount < self.balance or amount == self.balance:
            print(f'Успешно выведено с аккаунта {self.name} на аккаунт {target_account}')
            after_transwer = self.balance - amount
            print(f'Остаток на балансе {after_transwer} рублей')

    def my_balance(self):
        print(f'Ваш баланс {self.balance} рублей')


elshad = BankAccount('ELshad', 3000)
elshad_balance = elshad.my_balance()
# elshad_deposit = elshad.replenishment(150)
# elshad_withdraw = elshad.withdraw(50)
# elshad_transwer = elshad.transwer(10,'Igor')
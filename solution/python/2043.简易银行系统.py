"""2043. 简易银行系统"""


class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.withdraw(account1, money):
            return False
        self.deposit(account2, money)
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not 1 <= account <= len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not 1 <= account <= len(self.balance) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


if __name__ == "__main__":
    test_cases = [([10, 100, 20, 50, 30],)]
    for _, (args,) in enumerate(test_cases):
        bank = Bank(args)
        assert bank.withdraw(3, 10)
        assert bank.transfer(5, 1, 20)

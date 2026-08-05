"""2043. 简易银行系统"""


class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance

    def _valid(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            not self._valid(account1)
            or not self._valid(account2)
            or self.balance[account1 - 1] < money
        ):
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


test_cases = [
    (
        [10, 100, 20, 50, 30],
        [("withdraw", (3, 10), True), ("transfer", (5, 1, 20), True)],
    ),
]


if __name__ == "__main__":
    for index, (balance, operations) in enumerate(test_cases):
        assert index == 0
        assert balance == [10, 100, 20, 50, 30]
        assert operations[0][0] == "withdraw"
    bank = Bank([10, 100, 20, 50, 30])
    assert bank.withdraw(3, 10)
    assert bank.transfer(5, 1, 20)
    assert not bank.deposit(6, 10)

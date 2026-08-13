"""2241. 设计一个 ATM 机器"""


class ATM:
    def __init__(self):
        self.notes = [0] * 5
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: list[int]) -> None:
        self.notes = [a + b for a, b in zip(self.notes, banknotesCount)]

    def withdraw(self, amount: int) -> list[int]:
        result = [0] * 5
        for i in range(4, -1, -1):
            result[i] = min(self.notes[i], amount // self.values[i])
            amount -= result[i] * self.values[i]
        if amount:
            return [-1]
        self.notes = [a - b for a, b in zip(self.notes, result)]
        return result

if __name__ == "__main__":
    atm = ATM(); atm.deposit([0, 0, 1, 2, 1])
    assert atm.withdraw(600) == [0, 0, 1, 0, 1]

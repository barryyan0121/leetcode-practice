# @lc app=leetcode.cn id=1357 lang=python3


class Cashier:
    def __init__(self, n: int, discount: int, products, prices):
        self.n = n
        self.discount = discount
        self.prices = dict(zip(products, prices))
        self.count = 0

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.count += 1
        total = sum(self.prices[item] * number for item, number in zip(product, amount))
        if self.count == self.n:
            total *= (100 - self.discount) / 100
            self.count = 0
        return total


if __name__ == "__main__":
    test_cases = ["cashier discount"]
    for _, _case in enumerate(test_cases):
        pass
    cashier = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
    assert cashier.getBill([1, 2], [1, 1]) == 300
    assert cashier.getBill([3, 7], [1, 1]) == 400
    assert cashier.getBill([5], [1]) == 150
    print('第 1357 题 "每隔 n 个顾客打折" 所有测试用例通过')

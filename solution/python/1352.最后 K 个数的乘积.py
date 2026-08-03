# @lc app=leetcode.cn id=1352 lang=python3


class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]


if __name__ == "__main__":
    test_cases = ["prefix product"]
    for _, _case in enumerate(test_cases):
        pass
    product = ProductOfNumbers()
    product.add(3)
    product.add(0)
    product.add(2)
    product.add(5)
    product.add(4)
    assert product.getProduct(2) == 20
    assert product.getProduct(3) == 40
    assert product.getProduct(4) == 0
    print('第 1352 题 "最后 K 个数的乘积" 所有测试用例通过')

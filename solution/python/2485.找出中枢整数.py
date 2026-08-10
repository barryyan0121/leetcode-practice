"""2485. 找出中枢整数"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        pivot = int(total**0.5)
        return pivot if pivot * pivot == total else -1

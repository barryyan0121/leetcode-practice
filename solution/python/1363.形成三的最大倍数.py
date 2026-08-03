# @lc app=leetcode.cn id=1363 lang=python3

from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        counts = [0] * 10
        for digit in digits:
            counts[digit] += 1
        total = sum(digit * counts[digit] for digit in range(10))

        def remove(remainder: int, amount: int) -> bool:
            for digit in range(1, 10):
                if digit % 3 == remainder and counts[digit] >= amount:
                    counts[digit] -= amount
                    return True
            return False

        remainder = total % 3
        if remainder == 1:
            if not remove(1, 1) and not remove(2, 2):
                return ""
        elif remainder == 2:
            if not remove(2, 1) and not remove(1, 2):
                return ""
        result = "".join(str(digit) * counts[digit] for digit in range(9, -1, -1))
        return result if result and result[0] != "0" else ("0" if result else "")


if __name__ == "__main__":
    test_cases = [
        (Solution().largestMultipleOfThree, ([8, 1, 9],), "981"),
        (Solution().largestMultipleOfThree, ([8, 6, 7, 1, 0],), "8760"),
        (Solution().largestMultipleOfThree, ([1],), ""),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1363 题 "形成三的最大倍数" 所有测试用例通过')

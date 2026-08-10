"""2197. 替换数组中的非互质数"""

from math import gcd


class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack = []
        for value in nums:
            stack.append(value)
            while len(stack) > 1:
                divisor = gcd(stack[-1], stack[-2])
                if divisor == 1:
                    break
                stack[-2:] = [stack[-1] // divisor * stack[-2]]
        return stack


if __name__ == "__main__":
    assert Solution().replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2]) == [12, 7, 6]

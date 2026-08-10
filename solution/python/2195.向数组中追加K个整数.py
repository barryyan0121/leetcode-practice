"""2195. 向数组中追加 K 个整数"""


class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        total = 0
        current = 1
        for value in sorted(set(nums)):
            if current < value:
                count = min(k, value - current)
                total += (current + current + count - 1) * count // 2
                k -= count
                if not k:
                    return total
            current = max(current, value + 1)
        return total + (current + current + k - 1) * k // 2


if __name__ == "__main__":
    assert Solution().minimalKSum([1, 4, 25, 10, 25], 2) == 5

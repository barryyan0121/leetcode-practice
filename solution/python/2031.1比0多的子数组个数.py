"""2031. 1 比 0 多的子数组个数"""


class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        offset = len(nums) + 1
        bit = [0] * (2 * offset + 3)

        def add(index: int) -> None:
            while index < len(bit):
                bit[index] += 1
                index += index & -index

        def query(index: int) -> int:
            result = 0
            while index:
                result += bit[index]
                index -= index & -index
            return result

        prefix = offset
        add(prefix)
        answer = 0
        for value in nums:
            prefix += 1 if value else -1
            answer = (answer + query(prefix - 1)) % mod
            add(prefix)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 1, 0, 0, 1],), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().subarraysWithMoreOnesThanZeroes(*args) == expected

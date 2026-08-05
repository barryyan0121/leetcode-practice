"""2654. 使数组为空的最少操作次数"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        from collections import Counter

        answer = 0
        for count in Counter(nums).values():
            if count == 1:
                return -1
            answer += (count + 2) // 3
        return answer


if __name__ == "__main__":
    test_cases = [(([2, 3, 3, 2, 2, 4, 2, 3, 4],), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected

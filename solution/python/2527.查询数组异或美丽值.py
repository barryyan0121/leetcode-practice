"""2527. 查询数组异或美丽值"""


class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        answer = 0
        for value in nums:
            answer ^= value
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 4],), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().xorBeauty(*args) == expected

"""2541. 使数组中所有元素相等的最小操作数 II"""


class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        operations = 0
        balance = 0
        for first, second in zip(nums1, nums2):
            difference = first - second
            if difference % k:
                return -1
            balance += difference
            if difference > 0:
                operations += difference // k
        return operations if balance == 0 else -1


if __name__ == "__main__":
    test_cases = [(([4, 3, 1], [2, 4, 2], 1), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected

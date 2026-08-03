# @lc app=leetcode.cn id=1577 lang=python3


class Solution:
    def numTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        def count(a: list[int], b: list[int]) -> int:
            result = 0
            for x in a:
                freq = {}
                for y in b:
                    if x * x % y == 0:
                        z = x * x // y
                        result += freq.get(z, 0)
                    freq[y] = freq.get(y, 0) + 1
            return result

        return count(nums1, nums2) + count(nums2, nums1)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numTriplets, ([7, 4], [5, 2, 8, 9]), 1),
        (solution.numTriplets, ([1, 1], [1, 1, 1]), 9),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1577 题 "数的平方等于两数乘积的方法数" 所有测试用例通过')

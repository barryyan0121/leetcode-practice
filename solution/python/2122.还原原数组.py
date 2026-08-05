"""2122. 还原原数组"""


class Solution:
    def recoverArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums) // 2
        smallest = nums[0]
        for index in range(1, len(nums)):
            difference = nums[index] - smallest
            if difference <= 0 or difference % 2:
                continue
            k = difference // 2
            counts = {}
            for value in nums:
                counts[value] = counts.get(value, 0) + 1
            result = []
            valid = True
            for value in nums:
                if counts.get(value, 0) == 0:
                    continue
                counts[value] -= 1
                if counts.get(value + 2 * k, 0) == 0:
                    valid = False
                    break
                counts[value + 2 * k] -= 1
                result.append(value + k)
            if valid and len(result) == n:
                return result
        return []


if __name__ == "__main__":
    test_cases = [(([2, 10, 6, 4, 8, 12],), [3, 7, 11])]
    for _, (args, expected) in enumerate(test_cases):
        assert sorted(Solution().recoverArray(*args)) == expected

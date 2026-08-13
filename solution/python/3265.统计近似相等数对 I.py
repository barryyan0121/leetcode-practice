"""3265. 统计近似相等数对 I"""


class Solution:
    def countPairs(self, nums: list[int]) -> int:
        def almost_equal(left: int, right: int) -> bool:
            width = max(len(str(left)), len(str(right)))
            left_digits = list(str(left).zfill(width))
            right_digits = list(str(right).zfill(width))
            mismatches = [
                index
                for index, (a, b) in enumerate(zip(left_digits, right_digits))
                if a != b
            ]
            if not mismatches:
                return True
            if len(mismatches) != 2:
                return False
            first, second = mismatches
            return (
                left_digits[first] == right_digits[second]
                and left_digits[second] == right_digits[first]
            )

        answer = 0
        for index, left in enumerate(nums):
            for right in nums[index + 1 :]:
                if almost_equal(left, right):
                    answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        ([3, 12, 30, 17, 21], 2),
        ([1, 1, 1, 1, 1], 10),
        ([123, 231], 0),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().countPairs(nums) == expected

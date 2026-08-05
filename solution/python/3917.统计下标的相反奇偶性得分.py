"""3917. 统计下标的相反奇偶性得分"""


class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odd = sum(value % 2 for value in nums)
        even = len(nums) - odd
        answer = []
        for value in nums:
            if value % 2:
                odd -= 1
                answer.append(even)
            else:
                even -= 1
                answer.append(odd)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 4],), [2, 1, 1, 0]), (([1],), [0])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countOppositeParity(*args) == expected

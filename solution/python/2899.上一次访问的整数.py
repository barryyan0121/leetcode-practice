"""2899. 上一次访问的整数"""


class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        values = []
        next_index = 0
        answer = []
        for value in nums:
            if value == -1:
                if next_index:
                    next_index -= 1
                    answer.append(values[next_index])
                else:
                    answer.append(-1)
            else:
                values.append(value)
                next_index = len(values)
        return answer


if __name__ == "__main__":
    assert Solution().lastVisitedIntegers([1, 2, -1, -1, -1, 3, -1]) == [2, 1, -1, 3]

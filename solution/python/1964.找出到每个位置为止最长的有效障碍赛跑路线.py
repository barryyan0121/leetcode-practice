"""1964. 找出到每个位置为止最长的有效障碍赛跑路线"""

from bisect import bisect_right


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        tails = []
        answer = []
        for value in obstacles:
            index = bisect_right(tails, value)
            if index == len(tails):
                tails.append(value)
            else:
                tails[index] = value
            answer.append(index + 1)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 2],), [1, 2, 3, 3]), (([2, 2, 1],), [1, 2, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().longestObstacleCourseAtEachPosition(*args) == expected

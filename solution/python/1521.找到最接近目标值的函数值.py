# @lc app=leetcode.cn id=1521 lang=python3


class Solution:
    def closestToTarget(self, arr: list[int], target: int) -> int:
        previous = []
        answer = 10**9
        for value in arr:
            current = [value]
            for previous_value in previous:
                combined = previous_value & value
                if combined != current[-1]:
                    current.append(combined)
            answer = min(answer, *(abs(value - target) for value in current))
            previous = current
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.closestToTarget, ([9, 12, 3, 7, 15], 5), 2)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1521 题 "找到最接近目标值的函数值" 所有测试用例通过')

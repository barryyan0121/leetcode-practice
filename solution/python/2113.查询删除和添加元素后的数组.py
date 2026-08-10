"""2113. 查询删除和添加元素后的数组"""


class Solution:
    def elementInNums(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        cycle = 2 * n
        answer = []
        for time, index in queries:
            if index >= n:
                answer.append(-1)
                continue
            phase = time % cycle
            length = n - phase if phase < n else phase - n
            answer.append(
                nums[phase + index]
                if phase < n and index < length
                else nums[index] if phase >= n and index < length else -1
            )
        return answer


if __name__ == "__main__":
    test_cases = [(([0, 1, 2], [[0, 2], [2, 0], [3, 2], [5, 0]]), [2, 2, -1, 0])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().elementInNums(*args) == expected

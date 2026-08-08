class Solution:
    def findLatestStep(self, arr: list[int], m: int) -> int:
        length = [0] * (len(arr) + 2)
        groups = [0] * (len(arr) + 1)
        answer = -1
        for step, position in enumerate(arr, 1):
            left, right = length[position - 1], length[position + 1]
            if left:
                groups[left] -= 1
            if right:
                groups[right] -= 1
            total = left + right + 1
            length[position - left] = length[position + right] = total
            groups[total] += 1
            if groups[m]:
                answer = step
        return answer


if __name__ == "__main__":
    test_cases = [([3, 5, 1, 2, 4], 1, 4), ([3, 1, 5, 4, 2], 2, -1)]
    for _, (arr, m, expected) in enumerate(test_cases):
        assert Solution().findLatestStep(arr, m) == expected

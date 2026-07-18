class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        stack = [float("inf")]
        cost = 0
        for value in arr:
            while stack[-1] <= value:
                middle = stack.pop()
                cost += middle * min(stack[-1], value)
            stack.append(value)
        while len(stack) > 2:
            cost += stack.pop() * stack[-1]
        return cost


if __name__ == "__main__":
    test_cases = [
        ([6, 2, 4], 32),
        ([4, 11], 44),
        ([6, 6, 6], 72),
        ([15, 13, 5, 3, 15], 500),
    ]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().mctFromLeafValues(arr) == expected

"""2606. 找到最大开销的子字符串"""


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        costs = {char: value for char, value in zip(chars, vals)}
        answer = current = 0
        for char in s:
            current = max(0, current + costs.get(char, ord(char) - 96))
            answer = max(answer, current)
        return answer


if __name__ == "__main__":
    test_cases = [(("adaa", "d", [-1000]), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximumCostSubstring(*args) == expected

"""3019. 按键变更的次数"""


class Solution:
    def countKeyChanges(self, s: str) -> int:
        lowered = s.lower()
        return sum(left != right for left, right in zip(lowered, lowered[1:]))


if __name__ == "__main__":
    test_cases = [
        ("aAbBcC", 2),
        ("AaAaAaaA", 0),
    ]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().countKeyChanges(s) == expected

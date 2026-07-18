class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if any(char not in source for char in target):
            return -1
        index = answer = 0
        while index < len(target):
            answer += 1
            for char in source:
                if index < len(target) and char == target[index]:
                    index += 1
        return answer


if __name__ == "__main__":
    test_cases = [("abc", "abcbc", 2), ("abc", "acdbc", -1)]
    for _, (source, target, expected) in enumerate(test_cases):
        assert Solution().shortestWay(source, target) == expected

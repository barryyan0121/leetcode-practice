class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        distances = []
        for code in range(26):
            char = chr(97 + code)
            first = firstString.find(char)
            second = secondString.rfind(char)
            if first >= 0 and second >= 0:
                distances.append(first - second)
        if not distances:
            return 0
        minimum = min(distances)
        return distances.count(minimum)


if __name__ == "__main__":
    solution = Solution()
    assert solution.countQuadruples("abcd", "bccda") == 1
    assert solution.countQuadruples("ab", "cd") == 0
    print("1794 passed")

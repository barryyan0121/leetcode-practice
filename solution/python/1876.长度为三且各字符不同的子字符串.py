class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(len(set(s[index : index + 3])) == 3 for index in range(len(s) - 2))


if __name__ == "__main__":
    solution = Solution()
    assert solution.countGoodSubstrings("xyzzaz") == 1
    print("1876 passed")

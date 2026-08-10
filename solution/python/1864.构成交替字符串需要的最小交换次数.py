class Solution:
    def minSwaps(self, s: str) -> int:
        zeros, ones = s.count("0"), s.count("1")
        if abs(zeros - ones) > 1:
            return -1

        def mismatches(start: str) -> int:
            return sum(
                char != (start if index % 2 == 0 else ("1" if start == "0" else "0"))
                for index, char in enumerate(s)
            )

        if zeros > ones:
            return mismatches("0") // 2
        if ones > zeros:
            return mismatches("1") // 2
        return min(mismatches("0"), mismatches("1")) // 2


if __name__ == "__main__":
    solution = Solution()
    assert solution.minSwaps("111000") == 1
    print("1864 passed")

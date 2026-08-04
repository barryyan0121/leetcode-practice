class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = zeros = ones = answer = 0
        for right, character in enumerate(s):
            if character == "0":
                zeros += 1
            else:
                ones += 1
            while zeros > k and ones > k:
                if s[left] == "0":
                    zeros -= 1
                else:
                    ones -= 1
                left += 1
            answer += right - left + 1
        return answer


if __name__ == "__main__":
    test_cases = [(("10101", 1), 12), (("1010101", 2), 25), (("11111", 1), 15)]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().countKConstraintSubstrings(s, k) == expected

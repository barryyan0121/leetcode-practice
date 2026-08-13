class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = ones = 0
        answer = ""
        for right, value in enumerate(s):
            ones += value == "1"
            while ones > k:
                ones -= s[left] == "1"
                left += 1
            if ones == k:
                while s[left] == "0":
                    left += 1
                candidate = s[left : right + 1]
                if (
                    not answer
                    or len(candidate) < len(answer)
                    or (len(candidate) == len(answer) and candidate < answer)
                ):
                    answer = candidate
        return answer


assert Solution().shortestBeautifulSubstring("100011001", 3) == "11001"
assert Solution().shortestBeautifulSubstring("1011", 2) == "11"

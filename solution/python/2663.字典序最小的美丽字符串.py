"""2663. 字典序最小的美丽字符串"""


class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        for index in range(len(s) - 1, -1, -1):
            for code in range(ord(s[index]) + 1, ord("a") + k):
                if index >= 1 and code == ord(s[index - 1]):
                    continue
                if index >= 2 and code == ord(s[index - 2]):
                    continue
                answer = list(s[:index]) + [chr(code)]
                for position in range(index + 1, len(s)):
                    for next_code in range(ord("a"), ord("a") + k):
                        if position >= 1 and next_code == ord(answer[position - 1]):
                            continue
                        if position >= 2 and next_code == ord(answer[position - 2]):
                            continue
                        answer.append(chr(next_code))
                        break
                return "".join(answer)
        return ""


if __name__ == "__main__":
    assert Solution().smallestBeautifulString("abcz", 26) == "abda"

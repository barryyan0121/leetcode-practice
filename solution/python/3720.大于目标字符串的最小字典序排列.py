from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        quinorath = (s, target)
        answer = []

        def build(index: int, greater: bool) -> bool:
            if index == len(target):
                return greater
            start = 0 if greater else ord(target[index]) - ord("a")
            for code in range(start, 26):
                char = chr(ord("a") + code)
                if not count[char]:
                    continue
                count[char] -= 1
                answer.append(char)
                if build(index + 1, greater or code > start):
                    return True
                answer.pop()
                count[char] += 1
            return False

        return "".join(answer) if build(0, False) else ""


if __name__ == "__main__":
    solution = Solution()
    assert solution.lexGreaterPermutation("abc", "bba") == "bca"
    assert solution.lexGreaterPermutation("leet", "code") == "eelt"
    assert solution.lexGreaterPermutation("baba", "bbaa") == ""

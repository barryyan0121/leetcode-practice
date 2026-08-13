"""3167. 更好的字符串压缩"""

from collections import Counter


class Solution:
    def betterCompression(self, compressed: str) -> str:
        cnt = Counter()
        i, n = 0, len(compressed)
        while i < n:
            j = i + 1
            x = 0
            while j < n and compressed[j].isdigit():
                x = x * 10 + int(compressed[j])
                j += 1
            cnt[compressed[i]] += x
            i = j
        return "".join(f"{k}{v}" for k, v in sorted(cnt.items()))


if __name__ == "__main__":
    f = Solution().betterCompression
    assert f("a3c9b2c1") == "a3b2c10"
    assert f("c2b3a1") == "a1b3c2"

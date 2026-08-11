"""3006. 在给定数组中寻找美丽下标 I"""

from bisect import bisect_left


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        first = [i for i in range(len(s)) if s.startswith(a, i)]
        second = [i for i in range(len(s)) if s.startswith(b, i)]
        return [
            i
            for i in first
            if (pos := bisect_left(second, i - k)) < len(second)
            and second[pos] <= i + k
        ]


if __name__ == "__main__":
    assert Solution().beautifulIndices(
        "isawsquirrelnearmysquirrel", "my", "squirrel", 15
    ) == [16]

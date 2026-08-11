"""3008. 在给定数组中寻找美丽下标 II"""

from bisect import bisect_left


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        first = [i for i in range(len(s)) if s.startswith(a, i)]
        second = [i for i in range(len(s)) if s.startswith(b, i)]
        answer = []
        for index in first:
            pos = bisect_left(second, index - k)
            if pos < len(second) and second[pos] <= index + k:
                answer.append(index)
        return answer


if __name__ == "__main__":
    assert Solution().beautifulIndices("isawsquirrelnearmysquirrel", "my", "squirrel", 15) == [16]

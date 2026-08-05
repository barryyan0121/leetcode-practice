class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(x: str, y: str) -> str:
            if y in x:
                return x
            for overlap in range(min(len(x), len(y)), -1, -1):
                if x.endswith(y[:overlap]):
                    return x + y[overlap:]

        ans = None
        for order in ((a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)):
            value = merge(merge(order[0], order[1]), order[2])
            if ans is None or (len(value), value) < (len(ans), ans):
                ans = value
        return ans


if __name__ == "__main__":
    assert Solution().minimumString("abc", "bca", "aaa") == "aaabca"

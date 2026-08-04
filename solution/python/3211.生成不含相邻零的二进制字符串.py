class Solution:
    def validStrings(self, n: int) -> list[str]:
        answer = []

        def build(prefix: str) -> None:
            if len(prefix) == n:
                answer.append(prefix)
                return
            build(prefix + "1")
            if not prefix or prefix[-1] == "1":
                build(prefix + "0")

        build("")
        return answer


if __name__ == "__main__":
    test_cases = [(1, ["1", "0"]), (3, ["111", "110", "101", "011", "010"])]
    for _, (n, expected) in enumerate(test_cases):
        assert set(Solution().validStrings(n)) == set(expected)

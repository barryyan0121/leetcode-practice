"""1952. 三除数"""


class Solution:
    def isThree(self, n: int) -> bool:
        root = int(n**0.5)
        return (
            root * root == n
            and root > 1
            and all(root % d for d in range(2, int(root**0.5) + 1))
        )


if __name__ == "__main__":
    test_cases = [((4,), True), ((2,), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isThree(*args) == expected

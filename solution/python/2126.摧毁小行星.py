"""2126. 摧毁小行星"""


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        for asteroid in sorted(asteroids):
            if mass < asteroid:
                return False
            mass += asteroid
        return True


if __name__ == "__main__":
    test_cases = [((10, [3, 9, 19, 5, 21]), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().asteroidsDestroyed(*args) == expected

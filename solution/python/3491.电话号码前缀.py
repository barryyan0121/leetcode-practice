class Solution:
    def phonePrefix(self, numbers: list[str]) -> bool:
        numbers.sort()
        return all(
            not numbers[index + 1].startswith(numbers[index])
            for index in range(len(numbers) - 1)
        )


if __name__ == "__main__":
    test_cases = [
        ((["1", "2", "4", "3"],), True),
        ((["001", "007", "15", "00153"],), False),
    ]
    for _, ((numbers,), expected) in enumerate(test_cases):
        assert Solution().phonePrefix(numbers) == expected

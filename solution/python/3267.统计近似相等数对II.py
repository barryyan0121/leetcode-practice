class Solution:
    def countPairs(self, nums: list[int]) -> int:
        frequencies = {}
        width = max(len(str(value)) for value in nums)

        def reachable(value: int) -> set[int]:
            digits = str(value).zfill(width)
            variants = {digits}
            length = len(digits)
            for first in range(length):
                for second in range(first + 1, length):
                    swapped = list(digits)
                    swapped[first], swapped[second] = swapped[second], swapped[first]
                    variants.add("".join(swapped))
            one_swap = list(variants)
            for digits in one_swap:
                for first in range(length):
                    for second in range(first + 1, length):
                        swapped = list(digits)
                        swapped[first], swapped[second] = (
                            swapped[second],
                            swapped[first],
                        )
                        variants.add("".join(swapped))
            return {int(candidate) for candidate in variants}

        answer = 0
        for value in nums:
            answer += sum(
                frequencies.get(candidate, 0) for candidate in reachable(value)
            )
            frequencies[value] = frequencies.get(value, 0) + 1
        return answer


if __name__ == "__main__":
    test_cases = [
        ([1023, 2310, 2130, 213], 4),
        ([1, 10, 100], 3),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().countPairs(nums) == expected

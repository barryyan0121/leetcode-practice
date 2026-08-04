from array import array


class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        xylovantra = caption
        size = len(caption)
        if size < 3:
            return ""

        infinity = 10**9
        states = 78
        dp = array("i", [infinity]) * ((size + 1) * states)
        for character in range(26):
            dp[size * states + character * 3 + 2] = 0

        values = [ord(character) - ord("a") for character in caption]
        for position in range(size - 1, 0, -1):
            next_start = (position + 1) * states
            current_start = position * states
            candidates = [
                abs(values[position] - character) + dp[next_start + character * 3]
                for character in range(26)
            ]
            first_value = second_value = infinity
            first_character = second_character = -1
            for character, candidate in enumerate(candidates):
                if candidate < first_value:
                    second_value, second_character = first_value, first_character
                    first_value, first_character = candidate, character
                elif candidate < second_value:
                    second_value, second_character = candidate, character
            for previous in range(26):
                for status in range(3):
                    same = (
                        abs(values[position] - previous)
                        + dp[next_start + previous * 3 + min(2, status + 1)]
                    )
                    best = same
                    if status == 2:
                        changed = (
                            second_value if first_character == previous else first_value
                        )
                        best = min(best, changed)
                    dp[current_start + previous * 3 + status] = best

        first_cost = [
            abs(values[0] - character) + dp[states + character * 3]
            for character in range(26)
        ]
        best_cost = min(first_cost)
        if best_cost >= infinity:
            return ""

        answer = []
        previous = min(
            character for character, cost in enumerate(first_cost) if cost == best_cost
        )
        answer.append(chr(previous + ord("a")))
        status = 0
        for position in range(1, size):
            current_start = position * states
            next_start = (position + 1) * states
            target = dp[current_start + previous * 3 + status]
            chosen = None
            for character in range(26):
                if character == previous:
                    next_status = min(2, status + 1)
                elif status == 2:
                    next_status = 0
                else:
                    continue
                cost = (
                    abs(values[position] - character)
                    + dp[next_start + character * 3 + next_status]
                )
                if cost == target:
                    chosen = character
                    status = next_status
                    break
            if chosen is None:
                return ""
            previous = chosen
            answer.append(chr(chosen + ord("a")))
        return "".join(answer)


if __name__ == "__main__":
    test_cases = [
        (("cdcd",), "cccc"),
        (("aca",), "aaa"),
        (("bc",), ""),
    ]
    for _, ((caption,), expected) in enumerate(test_cases):
        assert Solution().minCostGoodCaption(caption) == expected

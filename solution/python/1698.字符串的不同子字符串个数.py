class Solution:
    def countDistinct(self, s: str) -> int:
        transitions = [{}]
        links = [-1]
        lengths = [0]
        last = 0
        for char in s:
            current = len(transitions)
            transitions.append({})
            lengths.append(lengths[last] + 1)
            links.append(0)
            previous = last
            while previous >= 0 and char not in transitions[previous]:
                transitions[previous][char] = current
                previous = links[previous]
            if previous < 0:
                links[current] = 0
            else:
                target = transitions[previous][char]
                if lengths[previous] + 1 == lengths[target]:
                    links[current] = target
                else:
                    clone = len(transitions)
                    transitions.append(transitions[target].copy())
                    lengths.append(lengths[previous] + 1)
                    links.append(links[target])
                    while previous >= 0 and transitions[previous].get(char) == target:
                        transitions[previous][char] = clone
                        previous = links[previous]
                    links[target] = links[current] = clone
            last = current
        return sum(
            lengths[state] - lengths[links[state]]
            for state in range(1, len(transitions))
        )


if __name__ == "__main__":
    test_cases = [("aabbaba", 21), ("abcdefg", 28), ("", 0)]
    for index, (s, expected) in enumerate(test_cases):
        assert Solution().countDistinct(s) == expected, index

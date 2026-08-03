class Solution:
    def stringIndices(
        self, wordsContainer: list[str], wordsQuery: list[str]
    ) -> list[int]:
        children = [{}]
        best = [0]

        def better(first: int, second: int) -> int:
            if len(wordsContainer[first]) != len(wordsContainer[second]):
                return (
                    first
                    if len(wordsContainer[first]) < len(wordsContainer[second])
                    else second
                )
            return min(first, second)

        for index, word in enumerate(wordsContainer):
            node = 0
            best[0] = better(best[0], index)
            for character in reversed(word):
                if character not in children[node]:
                    children[node][character] = len(children)
                    children.append({})
                    best.append(index)
                node = children[node][character]
                best[node] = better(best[node], index)

        answer = []
        for word in wordsQuery:
            node = 0
            result = best[0]
            for character in reversed(word):
                if character not in children[node]:
                    break
                node = children[node][character]
                result = best[node]
            answer.append(result)
        return answer


if __name__ == "__main__":
    test_cases = [
        ((["abcd", "bcd", "xbcd"], ["cd", "bcd", "xyz"]), [1, 1, 1]),
        ((["abcdefgh", "poiuygh", "ghghgh"], ["gh", "acbfgh", "acbfegh"]), [2, 0, 2]),
    ]
    for _, ((container, query), expected) in enumerate(test_cases):
        assert Solution().stringIndices(container, query) == expected

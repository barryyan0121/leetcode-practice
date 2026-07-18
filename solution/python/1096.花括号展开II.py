class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        index = 0

        def parse_union() -> set[str]:
            nonlocal index
            result = parse_concatenation()
            while index < len(expression) and expression[index] == ",":
                index += 1
                result |= parse_concatenation()
            return result

        def parse_concatenation() -> set[str]:
            nonlocal index
            result = {""}
            while index < len(expression) and expression[index] not in ",}":
                if expression[index] == "{":
                    index += 1
                    options = parse_union()
                    index += 1
                else:
                    options = {expression[index]}
                    index += 1
                result = {prefix + suffix for prefix in result for suffix in options}
            return result

        return sorted(parse_union())


if __name__ == "__main__":
    test_cases = [
        ("{a,b}{c,{d,e}}", ["ac", "ad", "ae", "bc", "bd", "be"]),
        ("{{a,z},a{b,c},{ab,z}}", ["a", "ab", "ac", "z"]),
        ("{a,b}c{d,e}f", ["acdf", "acef", "bcdf", "bcef"]),
        ("abcd", ["abcd"]),
        ("{{a,b},{b,c}}", ["a", "b", "c"]),
    ]
    for _, (expression, expected) in enumerate(test_cases):
        assert Solution().braceExpansionII(expression) == expected

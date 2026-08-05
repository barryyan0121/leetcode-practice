import re


class Solution:
    def applySubstitutions(self, replacements: list[list[str]], text: str) -> str:
        values = dict(replacements)
        expanded = {}

        def expand(key: str) -> str:
            if key not in expanded:
                expanded[key] = re.sub(
                    r"%([A-Z])%",
                    lambda match: expand(match.group(1)),
                    values[key],
                )
            return expanded[key]

        return re.sub(r"%([A-Z])%", lambda match: expand(match.group(1)), text)


if __name__ == "__main__":
    test_cases = [
        (([["A", "abc"], ["B", "def"]], "%A%_%B%"), "abc_def"),
        (
            (([["A", "bce"], ["B", "ace"], ["C", "abc%B%"]], "%A%_%B%_%C%")),
            "bce_ace_abcace",
        ),
    ]
    for _, ((replacements, text), expected) in enumerate(test_cases):
        assert Solution().applySubstitutions(replacements, text) == expected

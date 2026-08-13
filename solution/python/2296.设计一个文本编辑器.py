"""2296. 设计一个文本编辑器"""


class TextEditor:
    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        count = min(k, len(self.left))
        del self.left[-count:]
        return count

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop())
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.pop())
        return "".join(self.left[-10:])


if __name__ == "__main__":
    editor = TextEditor()
    editor.addText("leetcode")
    assert editor.deleteText(4) == 4
    editor.addText("practice")
    assert editor.cursorLeft(3) == "leetpract"

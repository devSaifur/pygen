from enum import Enum

TextType = Enum("TextType", ["normal", "bold", "italic", "code", "links", "images"])


class TextNode:
    def __init__(self, text, text_type: Enum, url=None) -> None:
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, value: object) -> bool:
        if isinstance(value, TextNode):
            return (
                self.text == value.text
                and self.text_type == value.text_type
                and self.url == value.url
            )
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    text = text_node.text
    url = text_node.url
    text_type = text_node.text_type

    match text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text, props={"href": url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": url, "alt": text})
        case _:
            raise ValueError(f"Unsupported TextType: {text_type}")

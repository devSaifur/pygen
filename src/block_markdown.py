from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


class MarkdownBlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_html_node(markdown: str):
    md_blocks = markdown_to_blocks(markdown)
    children = []

    for block in md_blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    return ParentNode("div", children)


def block_to_html_node(block: str):
    block_type = block_to_block_type(block)

    if block_type == MarkdownBlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    elif block_type == MarkdownBlockType.HEADING:
        return heading_to_html_node(block)
    elif block_type == MarkdownBlockType.QUOTE:
        return quote_to_html_node(block)
    elif block_type == MarkdownBlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    elif block_type == MarkdownBlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    elif block_type == MarkdownBlockType.CODE:
        return code_to_html_node(block)
    else:
        raise ValueError("Invalid block type")


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def block_to_block_type(block: str) -> MarkdownBlockType:
    lines = block.strip().split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return MarkdownBlockType.HEADING

    if len(lines) > 1 and block.startswith("```") and block.endswith("```"):
        return MarkdownBlockType.CODE

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return MarkdownBlockType.PARAGRAPH
        return MarkdownBlockType.QUOTE

    if block.startswith("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") and not line.startswith("- "):
                return MarkdownBlockType.PARAGRAPH
        return MarkdownBlockType.UNORDERED_LIST

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return MarkdownBlockType.PARAGRAPH
            i += 1
        return MarkdownBlockType.ORDERED_LIST

    else:
        return MarkdownBlockType.PARAGRAPH

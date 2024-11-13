from textnode import TextNode, TextType


def main():
    text_node = TextNode("Hello World", TextType.TEXT, "https://www.google.com")
    print(text_node)


main()

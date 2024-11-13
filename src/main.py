from textnode import TextNode, TextType


def main():
    text_node = TextNode("Hello World", TextType.normal, "https://www.google.com")
    print(text_node)


main()

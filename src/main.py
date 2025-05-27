from textnode import *
from htmlnode import *

def main():
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)

    print(html_node.to_html())

main()

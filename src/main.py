from textnode import *
from htmlnode import *
from inline_markdown import *

def main():
    link_node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev). Thanks!",
        TextType.TEXT,
    )

    image_node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )

    new_link_nodes = split_nodes_link([link_node])
    new_image_nodes = split_nodes_image([image_node])

    print(f'{link_node}\n---------------\n')
    for node in new_link_nodes:
        print(node)
    print(f'\n\n{image_node}\n---------------\n')
    for node in new_image_nodes:
        print(node)
main()

from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    alt_text = re.findall(r"!\[[\w\s]+\]", text)
    for i in range(len(alt_text)):
        alt_text[i] = alt_text[i][2:][:-1]
    links = re.findall(r"\(([^\(\)]*)\)",text)

    return list(zip(alt_text, links))

def extract_markdown_links(text):
    anchors = re.findall(r"\[[\w\s]+\]", text)
    for i in range(len(anchors)):
        anchors[i] = anchors[i][1:][:-1]
    links = re.findall(r"\(([^\(\)]*)\)",text)

    return list(zip(anchors, links))

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        link_nodes = extract_markdown_links(node.text)
        start = 0
        end = 0
        for i in range(len(link_nodes)):
            end = node.text.find(link_nodes[i][0])-1
            if end != start:
                text = node.text[start:end]
                new_nodes.append(TextNode(text,TextType.TEXT))
            new_nodes.append(TextNode(link_nodes[i][0],TextType.LINK,link_nodes[i][1]))
            start = end + len(link_nodes[i][0]) + len(link_nodes[i][1]) + 4
        if start < len(node.text):
            text = node.text[start:]
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        image_nodes = extract_markdown_images(node.text)
        start = 0
        end = 0
        for i in range(len(image_nodes)):
            end = node.text.find(image_nodes[i][0])-2
            if end != start:
                text = node.text[start:end]
                new_nodes.append(TextNode(text,TextType.TEXT))
            new_nodes.append(TextNode(image_nodes[i][0],TextType.IMAGE,image_nodes[i][1]))
            start = end + len(image_nodes[i][0]) + len(image_nodes[i][1]) + 5
        if start < len(node.text):
            text = node.text[start:]
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
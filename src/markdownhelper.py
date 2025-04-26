import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        split_nodes = []
        split = node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise Exception('Invalid Markdown: must have a closing delimiter')
        for i in range(len(split)):
            if split[i] == "":
                continue
            if i % 2 != 0:
                split_nodes.append(TextNode(split[i], text_type))
            else:
                split_nodes.append(TextNode(split[i], TextType.TEXT))
        node_list.extend(split_nodes)
    return node_list

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        og_text = node.text
        split = extract_markdown_images(og_text)
        for image in split:
            sections = og_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                node_list.append(TextNode(sections[0], TextType.TEXT))
            node_list.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            og_text = sections[1]
        if og_text != "":
            node_list.append(TextNode(og_text, TextType.TEXT))
    return node_list

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        og_text = node.text
        split = extract_markdown_links(og_text)
        for link in split:
            sections = og_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                node_list.append(TextNode(sections[0], TextType.TEXT))
            node_list.append(TextNode(link[0], TextType.LINK, link[1]))
            og_text = sections[1]
        if og_text != "":
            node_list.append(TextNode(og_text, TextType.TEXT))
    return node_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
   return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [x.strip() for x in blocks if x.strip() != ""]
    return blocks
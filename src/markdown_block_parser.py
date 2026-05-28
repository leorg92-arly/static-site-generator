import re
from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean_blocks = []

    for block in blocks:
        stripped_block = block.strip()

        if stripped_block != "":
            clean_blocks.append(stripped_block)
    
    return clean_blocks

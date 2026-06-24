import re
from textnode import TextNode, TextType 


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]: 
    ret_list = []

    for node in old_nodes:
        nodes_text = node.text.split(delimiter)
        if(len(nodes_text) == 1):
            ret_list.append(node)
            continue

        if(len(nodes_text) % 2 == 0):
            raise Exception("Unmatched Delimiters")

        odd = True 
        for node_text in nodes_text:
            if node_text == "":
                continue
            if(odd):
                ret_list.append(TextNode(node_text, TextType.TEXT))
                odd = False
            else: 
                ret_list.append(TextNode(node_text, text_type))
                odd = True 

    
    return ret_list 

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

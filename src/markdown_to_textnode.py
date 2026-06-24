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
                odd = not odd
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

def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    ret_list = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if(len(images) == 0):
            ret_list.append(node)
            continue

        current_text = node.text

        for image in images: # (alt_text, link) tuple
            current_text_split = current_text.split(f"![{image[0]}]({image[1]})", 1)
            if(len(current_text_split) != 2):
                raise Exception("Something went wrong in matching the images to text")
            
            start = TextNode(current_text_split[0], TextType.TEXT)
            if(current_text_split[0] != ""):
                ret_list.append(start)

            curr_image = TextNode(image[0], TextType.IMAGE, image[1])
            ret_list.append(curr_image)

            current_text = current_text_split[1] 

        if(current_text != ""):
            last_text = TextNode(current_text, TextType.TEXT)
            ret_list.append(last_text)
    
    return ret_list 

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    ret_list = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if(len(links) == 0):
            ret_list.append(node)
            continue

        current_text = node.text

        for link in links: # (alt_text, link) tuple
            current_text_split = current_text.split(f"[{link[0]}]({link[1]})", 1)
            if(len(current_text_split) != 2):
                raise Exception("Something went wrong in matching the images to text")
            
            start = TextNode(current_text_split[0], TextType.TEXT)
            if(current_text_split[0] != ""):
                ret_list.append(start)

            curr_link = TextNode(link[0], TextType.LINK, link[1])
            ret_list.append(curr_link)

            current_text = current_text_split[1] 

        if(current_text != ""):
            last_text = TextNode(current_text, TextType.TEXT)
            ret_list.append(last_text)
    
    return ret_list 

def text_to_textnodes(text):

    textnode = TextNode(text, TextType.TEXT) 

    bold_list = split_nodes_delimiter([textnode], "**", TextType.BOLD)
    cold_list = split_nodes_delimiter(bold_list, "`", TextType.CODE)
    cild_list = split_nodes_delimiter(cold_list, "_", TextType.ITALIC)
    cild_list_img = split_nodes_images(cild_list)
    ret_list = split_nodes_link(cild_list_img)

    return ret_list

















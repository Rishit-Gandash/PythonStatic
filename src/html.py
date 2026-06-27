from htmlnode import HTMLNode, LeafNode, ParentNode
from blocks import markdown_to_blocks, block_to_block_type, BlockType
from markdown_to_textnode import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for i in textnodes:
        children.append(text_node_to_html_node(i))
    return children


def markdown_to_html_node(markdown_doc):
    markdown_blocks = markdown_to_blocks(markdown_doc)
    htmlnode_list = []

    for block in markdown_blocks:
        blocktype = block_to_block_type(block)
        if(blocktype == BlockType.QUOTE):
            block_text = block.split("\n")
            clean_text = ""
            for i in block_text:
                clean_text += i[2::]
                clean_text += " "

            children = text_to_children(clean_text[:-1:])
            htmlnode_list.append(ParentNode("blockquote", children))

        if(blocktype == BlockType.ULIST):
            block_text = block.split("\n")
            children = []
            for i in block_text:
                clean_text = ""
                clean_text += i[2::]
                list_item = text_to_children(clean_text)
                children.append(ParentNode("li", list_item))

            htmlnode_list.append(ParentNode("ul", children))


        if(blocktype == BlockType.OLIST):
            block_text = block.split("\n")
            children = []
            for i in block_text:
                clean_text = ""
                clean_text += i[3::]
                list_item = text_to_children(clean_text)
                children.append(ParentNode("li", list_item))

            htmlnode_list.append(ParentNode("ol", children))


        if(blocktype == BlockType.CODE):
            block = block[3:len(block) - 3:]
            if(block[0] == "\n"):
                block = block[1::]
            code_text = TextNode(block , TextType.CODE)
            code_node = text_node_to_html_node(code_text)
            htmlnode_list.append(ParentNode("pre", [code_node]))

        if(blocktype == BlockType.HEADING):
            h_lvl = 0 
            while(block[h_lvl] == "#"):
                h_lvl += 1

            children = text_to_children(block[h_lvl+1::])
            htmlnode_list.append(ParentNode(f"h{h_lvl}", children))

        if(blocktype == BlockType.PARA):
            blocks = block.split("\n")
            block = " ".join(blocks)
            children = text_to_children(block)
            htmlnode_list.append(ParentNode("p", children))

    return ParentNode("div", htmlnode_list)





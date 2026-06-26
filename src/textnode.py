from enum import Enum
from .htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    ITALIC = "italic"
    BOLD = "bold"
    CODE = "code" 
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if(self.text == other.text and
           self.url == other.url and
           self.text_type == other.text_type):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(textNode : TextNode) -> LeafNode:
    textType = textNode.text_type

    if(textType == TextType.TEXT):
        return LeafNode(None, textNode.text)
    if(textType == TextType.BOLD):
        return LeafNode("b", textNode.text)
    if(textType == TextType.ITALIC):
        return LeafNode("i", textNode.text)
    if(textType == TextType.CODE):
        return LeafNode("code", textNode.text) 
    if(textType == TextType.LINK):
        return LeafNode("a", textNode.text, {"href":textNode.url})
    if(textType == TextType.IMAGE):
        return LeafNode("img", "", {"src": textNode.url, "alt": textNode.text})

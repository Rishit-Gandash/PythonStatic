from enum import Enum

class BlockType(Enum):
    PARA = "para" 
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    block_list = markdown.split("\n\n")
    cnt = 0
    for i in range(len(block_list)):
        i -= cnt
        block_list[i] = block_list[i].strip()
        if block_list[i] == "":
            del block_list[i]
            cnt += 1 

    return block_list

def block_to_block_type(markdown_block):
    for i in range(1, 7): 
        start = "#" * i + " "
        if(markdown_block.startswith(start)):
            return BlockType.HEADING

    if(markdown_block.startswith("```") and markdown_block.endswith("```")):
        return BlockType.CODE

    block_list = markdown_block.split("\n")

    quote = True
    for line in block_list:
        if(not line.startswith(">")):
            quote = False 
            break

    if(quote):
        return BlockType.QUOTE


    ul = True
    for line in block_list:
        if(not line.startswith("- ")):
            ul = False 
            break

    if(ul):
        return BlockType.ULIST


    ol = True
    i = 1 
    for line in block_list:
        if(not line.startswith(f"{i}. ")):
            ol = False 
            break
        i += 1

    if(ol):
        return BlockType.OLIST

    return BlockType.PARA

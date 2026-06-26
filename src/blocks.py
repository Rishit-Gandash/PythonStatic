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
    if(markdown_block[0] == "#"):
        return BlockType.HEADING
    if(markdown_block[0] == "#"):
        return BlockType.HEADING

    if(markdown_block[0] == "#"):
        return BlockType.HEADING
    
    if(markdown_block[0] == "#"):
        return BlockType.HEADING
    
    if(markdown_block[0] == "#"):
        return BlockType.HEADING
    
    if(markdown_block[0] == "#"):
        return BlockType.HEADING
    
    if(markdown_block[0] == "#"):
        return BlockType.HEADING
    
    if(markdown_block[0] == "#"):
        return BlockType.HEADING
    
    
    

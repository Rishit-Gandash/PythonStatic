import re

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"


mage = extract_markdown_images(text)

current_text = text

current_text_split = current_text.split(f"![{image[0][0]}]({image[0][1]})")

print(current_text_split[0])
print(f"![{image[0][0]}]({image[0][1]})")
print(current_text_split[1])

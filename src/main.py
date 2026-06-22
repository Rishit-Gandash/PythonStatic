from .textnode import TextNode, TextType

def main():
    t1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(t1)


if __name__ == "__main__": 
    main()

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        '''

        An HTMLNode without a tag will just render as raw text
        An HTMLNode without a value will be assumed to have children
        An HTMLNode without children will be assumed to have a value
        An HTMLNode without props simply won't have any attributes

        '''

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if(self.props == None):
            return ""

        ret_val = ""

        for key, value in self.props.items():
            ret_val += f"{key}=\"{value}\" "

        if(ret_val[-1] == " "):
            ret_val = ret_val[:-1:]

        return ret_val

    def __repr__(self):
        return (
                f"<{self.tag}{' ' + self.props_to_html() if self.props else ''}>"
                f"{''.join(str(i) for i in self.children) if self.children else self.value}"
                f"</{self.tag}>"
            )

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if(self.value == None):
            raise ValueError
        if(self.tag == None):
            return self.value 
        
        return (
                f"<{self.tag}{' ' + self.props_to_html() if self.props else ''}>"
                f"{self.value}"
                f"</{self.tag}>"
            )

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if(self.children == None):
            raise ValueError("No Children")
        if(self.tag == None):
            raise ValueError("No Tag")
        
        return (
                f"<{self.tag}{' ' + self.props_to_html() if self.props else ''}>"
                f"{''.join(i.to_html() for i in self.children)}"
                f"</{self.tag}>"
            )

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

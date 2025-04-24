from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag can not be none")
        if self.children is None:
            raise ValueError("Node must have children")
        html_string = f"<{self.tag}>"
        for item in self.children:
            html_string += item.to_html()
        html_string += f"</{self.tag}>"
        return html_string

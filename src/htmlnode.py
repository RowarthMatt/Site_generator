class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        html = ""
        if self.props == None:
            return html
        for prop in self.props:
            html = html + f' {prop}="{self.props[prop]}"'
        return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leafnode must have a value")
        if self.tag is None:
            return self.value
        opening_tag = f"<{self.tag}"
        if self.props is not None:
            opening_tag += self.props_to_html()
        opening_tag += ">"
        closing_tag = f"</{self.tag}>"
        return opening_tag + self.value + closing_tag
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parnet node must have a tag")
        if self.children is None:
            raise ValueError("Parent node must have children nodes")
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


        
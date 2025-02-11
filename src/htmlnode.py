
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        html_str = ""
        if self.props == None:
            return html_str
        for prop in self.props:
            html_str += f' {prop}="{self.props[prop]}"'
        return html_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError('All leaves must have a value')
        if self.tag == None:
            return str(self.value)
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('Parent Node must have a tag!')
        if self.children == None:
            raise ValueError('No children detected on ParentNode!')
        html_children = list(map(lambda child: child.to_html(), self.children))
        return f'<{self.tag}>{"".join(html_children)}</{self.tag}>'
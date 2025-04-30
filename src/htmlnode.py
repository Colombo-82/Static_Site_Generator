class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        if children is None:
            children = []
        if props is None:
            props = {}
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML")
    
    def props_to_html(self):
        if self.props == {}:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
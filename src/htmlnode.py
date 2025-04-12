


class HTMLNode:
    def __init__(self, tag:str = None, value:str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    # TODO
    def props_to_html(self):
        pass
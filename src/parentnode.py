

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    # TODO: Keep working on this implementation. This will be recursive and may need a lot of work
    def to_html(self):
        if self.tag == None:
            raise ValueError("parent nodes must have a tag")
        if self.children == None or []:
            raise ValueError("parent nodes must have children")
        
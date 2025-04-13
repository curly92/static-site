import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_no_children(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_child_attribute(self):
        node = ParentNode(
        "p",
        [
            LeafNode("a", "Bold text", {"href":"https://example.com"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), '<p><a href="https://example.com">Bold text</a>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_with_parent_and_child_attribute(self):
        node = ParentNode(
        "p",
        [
            LeafNode("a", "Bold text", {"href":"https://example.com"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ], {"test_attribute":"attribute"}
        )
        self.assertEqual(node.to_html(), '<p test_attribute="attribute"><a href="https://example.com">Bold text</a>Normal text<i>italic text</i>Normal text</p>')
    
    def test_to_html_no_tag_exception(self):
        node = ParentNode(
        None,
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children_exception(self):
        node = ParentNode(
        "p",
        None,
        )
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
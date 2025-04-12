import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href":"http://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="http://example.com" target="_blank">Click Me!</a>')

    def test_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()
    def test_no_tag(self):
        node = LeafNode(None, "Hello!")
        self.assertEqual(node.to_html(), "Hello!")

if __name__ == "__main__":
    unittest.main()
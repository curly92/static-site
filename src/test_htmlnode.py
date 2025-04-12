import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props_to_hml(self):
        test_prop = HTMLNode("Test string", "Test value", None, None).props_to_html()
        self.assertEqual(test_prop, "")

    def test_props_to_html(self):
        test_prop = HTMLNode(
            "Test string", "Test value",
              None,
            {"href": "https://example.com"}).props_to_html()
        self.assertEqual(test_prop, ' href="https://example.com"')

    def test_mutliple_props_to_html(self):
        test_prop = HTMLNode(
            "Test string", "Test value",
              None,
            {"href": "https://example.com", "target":"_blank"}).props_to_html()
        self.assertEqual(test_prop, ' href="https://example.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()
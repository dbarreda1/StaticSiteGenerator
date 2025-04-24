import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    testProps = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    def test_eq(self):
        node = HTMLNode(props=self.testProps)
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
    
    def test_neq(self):
        node = HTMLNode(props=self.testProps)
        self.assertNotEqual(node.props_to_html(), 'href="https://www.google.net" target="_blank"')
    
    def test_repr(self):
        node = HTMLNode(props=self.testProps)
        self.assertIsNotNone(str(node))

if __name__ == "__main__":
    unittest.main()
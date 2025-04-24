import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is a text node", TextType.LINK, "http://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.LINK, "http://google.com")
        node2 = TextNode("This is a text node also", TextType.LINK, "http://google.com")
        self.assertNotEqual(node, node2)

    def test_text_to_html_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_img(self):
        node = TextNode("This is an image node", TextType.IMAGE, "http://google.com")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props_to_html(), 'src="http://google.com" alt="This is an image node"')


if __name__ == "__main__":
    unittest.main()
import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode('<p>','This is a test', None, props)
        result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), result)

    def test2(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "alt": "An image should be here!"
        }
        node = HTMLNode('<p>','This is a test', None, props)
        result = ' href="https://www.google.com" target="_blank" alt="An image should be here"'
        self.assertEqual(node.props_to_html(), result)

    def test2(self):
        node = HTMLNode('<p>','This is a test', None, None)
        result = ""
        self.assertEqual(node.props_to_html(), result)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


class TestParentNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()

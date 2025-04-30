import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_node_two_attribute(self):
        node = HTMLNode("div", "This is a div", children=[
            HTMLNode("p", "This is a paragraph"),
            HTMLNode("a", "This is a link", props={"href": "https://www.example.com"})
        ], props={"class": "my-class", "id": "my-id"})
        self.assertEqual(node.props_to_html(), ' class="my-class" id="my-id"')
    
    def test_node_one_attribute(self):
        node = HTMLNode("div", "This is a div", props={"class": "my-class"})
        self.assertEqual(node.props_to_html(), ' class="my-class"')

    def test_node_no_attribute(self):
        node = HTMLNode("div", "This is a div", props={})
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
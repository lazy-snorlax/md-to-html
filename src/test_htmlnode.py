import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
    def test_props_to_html2(self):
        node = HTMLNode(tag=None, props={"href": "https://www.google.com","target": "_blank", "disabled": True})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" disabled="True"')

    def test_props_to_html3(self):
        node = HTMLNode(tag=None, props={"href": "https://www.google.com","target": "_blank", "value": "This is a test"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" value="This is a test"')
    
    def test_leafnode(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leafnode2(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leafnode3(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(leaf.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')

    def test_parentnode1(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_parentnode2(self):
        node = ParentNode("p", [
            LeafNode("b", "Hello user!"),
            LeafNode("i", "Welcome to this page"),
            LeafNode("a", "Click here to start", {"href": "https://www.google.com", "target": "_blank"})
        ])
        # print(node.to_html())
        self.assertEqual(node.to_html(), '<p><b>Hello user!</b><i>Welcome to this page</i><a href="https://www.google.com" target="_blank">Click here to start</a></p>')

    def test_parentnode3(self):
        node = ParentNode("div", [
            LeafNode("b", "Hello user!"),
            LeafNode("i", "Welcome to this page"),
            LeafNode("a", "Click here to start", {"href": "https://www.google.com", "target": "_blank"}),
            ParentNode("div", [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ])
        ])
        # print(node.to_html())
        self.assertEqual(node.to_html(), '<div><b>Hello user!</b><i>Welcome to this page</i><a href="https://www.google.com" target="_blank">Click here to start</a><div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div></div>')

if __name__ == "__main__":
    unittest.main()
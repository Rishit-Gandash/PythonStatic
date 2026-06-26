import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNode(unittest.TestCase):

    def test_eq_1(self):
        attr = {
                "href":"boot.dev",
                "target":"_blank",
                "bizz": "bap",
                "long": "long",
            }
        node = HTMLNode("p", "want some dimsum", None, attr)
        tester = "href=\"boot.dev\" target=\"_blank\" bizz=\"bap\" long=\"long\""
        self.assertEqual(node.props_to_html(), tester)

    def test_eq_2(self):
        node = HTMLNode("p", "want some dimsum", None, None)
        tester = ""
        self.assertEqual(node.props_to_html(), tester)
    
    def test_eq_3(self):
        attr = {
                "href":"boot.dev",
                "target":"_blank",
            }
        node = HTMLNode("p", "want some dimsum", None, attr)
        tester = "href=\"boot.dev\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), tester)

    def test_leaf_to_html_p_boot(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!", {"href":"boot.dev"})
        self.assertEqual(node.to_html(), "<p href=\"boot.dev\">Hello, world!</p>")

    def test_leaf_to_html_no_p(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

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



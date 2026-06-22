import unittest
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq_1(self):
        attr = {
                "href":"boot.dev",
                "target":"_blank",
                "bizz": "bap",
                "long": "long",
            }
        node = HTMLNode("p", "want some dimsum", None, attr)
        print(node)
        tester = "href=\"boot.dev\" target=\"_blank\" bizz=\"bap\" long=\"long\""
        self.assertEqual(node.props_to_html(), tester)

    def test_eq_2(self):
        node = HTMLNode("p", "want some dimsum", None, None)
        tester = ""
        print(node)
        self.assertEqual(node.props_to_html(), tester)
    def test_eq_3(self):
        attr = {
                "href":"boot.dev",
                "target":"_blank",
            }
        node = HTMLNode("p", "want some dimsum", None, attr)
        tester = "href=\"boot.dev\" target=\"_blank\""
        print(node)
        self.assertEqual(node.props_to_html(), tester)

if __name__ == "__main__":
    unittest.main()



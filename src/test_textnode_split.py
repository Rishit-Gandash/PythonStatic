import unittest

from textnode import TextNode, TextType

from markdown_to_textnode import split_nodes_images, split_nodes_link



class TestSplitNodesImages(unittest.TestCase):

    def test_split_single_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            TextType.TEXT,
        )

        result = split_nodes_images([node])

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE,
                     "https://i.imgur.com/aKaOqIh.gif"),
        ]

        self.assertEqual(result, expected)

    def test_split_image_middle(self):
        node = TextNode(
            "before ![alt](image.jpg) after",
            TextType.TEXT,
        )

        result = split_nodes_images([node])

        expected = [
            TextNode("before ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "image.jpg"),
            TextNode(" after", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_split_multiple_images(self):
        node = TextNode(
            "a ![one](1.jpg) b ![two](2.jpg) c",
            TextType.TEXT,
        )

        result = split_nodes_images([node])

        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("one", TextType.IMAGE, "1.jpg"),
            TextNode(" b ", TextType.TEXT),
            TextNode("two", TextType.IMAGE, "2.jpg"),
            TextNode(" c", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_no_images(self):
        node = TextNode(
            "just plain text",
            TextType.TEXT,
        )

        result = split_nodes_images([node])

        self.assertEqual(result, [node])


class TestSplitNodesLinks(unittest.TestCase):

    def test_split_single_link(self):
        node = TextNode(
            "Click [Boot.dev](https://boot.dev)",
            TextType.TEXT,
        )

        result = split_nodes_link([node])

        expected = [
            TextNode("Click ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK,
                     "https://boot.dev"),
        ]

        self.assertEqual(result, expected)

    def test_split_link_middle(self):
        node = TextNode(
            "before [Google](https://google.com) after",
            TextType.TEXT,
        )

        result = split_nodes_link([node])

        expected = [
            TextNode("before ", TextType.TEXT),
            TextNode("Google", TextType.LINK,
                     "https://google.com"),
            TextNode(" after", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_split_multiple_links(self):
        node = TextNode(
            "a [one](1.com) b [two](2.com) c",
            TextType.TEXT,
        )

        result = split_nodes_link([node])

        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("one", TextType.LINK, "1.com"),
            TextNode(" b ", TextType.TEXT),
            TextNode("two", TextType.LINK, "2.com"),
            TextNode(" c", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_no_links(self):
        node = TextNode(
            "just plain text",
            TextType.TEXT,
        )

        result = split_nodes_link([node])

        self.assertEqual(result, [node])


if __name__ == "__main__":
    unittest.main()

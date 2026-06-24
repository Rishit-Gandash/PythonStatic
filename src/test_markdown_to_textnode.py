import unittest

from textnode import TextNode, TextType
from markdown_to_textnode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_no_delimiter(self):
        node = TextNode("this is plain text", TextType.TEXT)

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD
        )

        self.assertEqual(
            result,
            [TextNode("this is plain text", TextType.TEXT)]
        )

    def test_bold_delimiter(self):
        node = TextNode("this is **bold** text", TextType.TEXT)

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD
        )

        expected = [
            TextNode("this is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_italic_delimiter(self):
        node = TextNode("this is _italic_ text", TextType.TEXT)

        result = split_nodes_delimiter(
            [node],
            "_",
            TextType.ITALIC
        )

        expected = [
            TextNode("this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_code_delimiter(self):
        node = TextNode("use `print()` here", TextType.TEXT)

        result = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE
        )

        expected = [
            TextNode("use ", TextType.TEXT),
            TextNode("print()", TextType.CODE),
            TextNode(" here", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("hello **world**", TextType.TEXT),
            TextNode("plain text", TextType.TEXT),
        ]

        result = split_nodes_delimiter(
            nodes,
            "**",
            TextType.BOLD
        )

        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("plain text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_invalid_markdown(self):
        node = TextNode("this is **bold text", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter(
                [node],
                "**",
                TextType.BOLD
            )


    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_multiple_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertListEqual(expected, matches)

    def test_extract_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(expected, matches)



    def test_return_nothing(self):
        text = "[wonder_of_you]()"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_return_nothing_1(self):
        text = "[wonder_of_you](will find you)"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()

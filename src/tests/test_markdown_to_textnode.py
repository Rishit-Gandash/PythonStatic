import unittest

from src.textnode import TextNode, TextType
from src.markdown_to_textnode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, text_to_textnodes


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

    def test_plain_text(self):
        result = text_to_textnodes("just plain text")

        expected = [
            TextNode("just plain text", TextType.TEXT)
        ]

        self.assertEqual(result, expected)

    def test_bold_text(self):
        result = text_to_textnodes(
            "this is **bold** text"
        )

        expected = [
            TextNode("this is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_code_text(self):
        result = text_to_textnodes(
            "this is `code` text"
        )

        expected = [
            TextNode("this is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_italic_text(self):
        result = text_to_textnodes(
            "this is _italic_ text"
        )

        expected = [
            TextNode("this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_image(self):
        result = text_to_textnodes(
            "text ![rick](rick.png) more text"
        )

        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("rick", TextType.IMAGE, "rick.png"),
            TextNode(" more text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_link(self):
        result = text_to_textnodes(
            "go to [Boot.dev](https://boot.dev)"
        )

        expected = [
            TextNode("go to ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(result, expected)

    def test_mixed_markdown(self):
        result = text_to_textnodes(
            "This is **bold** and `code` and _italic_"
        )

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]

        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()

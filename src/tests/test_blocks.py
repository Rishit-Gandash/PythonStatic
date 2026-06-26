
import unittest
from src.blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_single_block(self):
        markdown = "Hello world"
        self.assertEqual(
            markdown_to_blocks(markdown),
            ["Hello world"]
        )

    def test_multiple_blocks(self):
        markdown = "Block one\n\nBlock two\n\nBlock three"
        self.assertEqual(
            markdown_to_blocks(markdown),
            ["Block one", "Block two", "Block three"]
        )

    def test_strip_whitespace(self):
        markdown = "  Block one  \n\n   Block two   "
        self.assertEqual(
            markdown_to_blocks(markdown),
            ["Block one", "Block two"]
        )

    def test_remove_empty_blocks(self):
        markdown = "Block one\n\n\n\nBlock two"
        self.assertEqual(
            markdown_to_blocks(markdown),
            ["Block one", "Block two"]
        )

    def test_leading_and_trailing_blank_lines(self):
        markdown = "\n\nBlock one\n\nBlock two\n\n"
        self.assertEqual(
            markdown_to_blocks(markdown),
            ["Block one", "Block two"]
        )

    def test_empty_string(self):
        markdown = ""
        self.assertEqual(
            markdown_to_blocks(markdown),
            []
            )

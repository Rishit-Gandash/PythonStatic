
import unittest
from src.blocks import markdown_to_blocks, block_to_block_type, BlockType


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

    # Block to block tests start here 

    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type("This is a paragraph."),
            BlockType.PARA
        )

    def test_heading_h1(self):
        self.assertEqual(
            block_to_block_type("# Heading"),
            BlockType.HEADING
        )

    def test_heading_h6(self):
        self.assertEqual(
            block_to_block_type("###### Heading"),
            BlockType.HEADING
        )

    def test_quote_single_line(self):
        self.assertEqual(
            block_to_block_type("> quoted text"),
            BlockType.QUOTE
        )

    def test_quote_multi_line(self):
        self.assertEqual(
            block_to_block_type("> line one\n> line two\n> line three"),
            BlockType.QUOTE
        )

    def test_unordered_list_single_item(self):
        self.assertEqual(
            block_to_block_type("- item"),
            BlockType.ULIST
        )

    def test_unordered_list_multiple_items(self):
        self.assertEqual(
            block_to_block_type("- item one\n- item two\n- item three"),
            BlockType.ULIST
        )

    def test_ordered_list(self):
        self.assertEqual(
            block_to_block_type(
                "1. first\n2. second\n3. third"
            ),
            BlockType.OLIST
        )

    def test_invalid_ordered_list(self):
        self.assertEqual(
            block_to_block_type(
                "1. first\n3. third"
            ),
            BlockType.PARA
        )

    def test_mixed_quote_and_text(self):
        self.assertEqual(
            block_to_block_type(
                "> quote\nnormal text"
            ),
            BlockType.PARA
        )

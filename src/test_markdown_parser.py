import unittest

from markdown_parser import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_split_bold(self):
        node = TextNode("This has **bold text** inside", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" inside", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_split_italic(self):
        node = TextNode("This has _italic text_ inside", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" inside", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_invalid_markdown_raises_exception(self):
        node = TextNode("This has **bold text without closing", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_non_text_nodes_are_preserved(self):

        node = TextNode("already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [node]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):

        node = TextNode("Start `code1` middle `code2` end", TextType.TEXT)

        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("code1", TextType.CODE),
            TextNode(" middle ", TextType.TEXT),
            TextNode("code2", TextType.CODE),
            TextNode(" end", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
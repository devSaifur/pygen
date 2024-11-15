import unittest
from gencontent import extract_md


class TestGenContent(unittest.TestCase):
    def test_gen_content(self):
        md = "# Hello, world!\n This is a paragraph. \n\n"
        self.assertEqual(extract_md(md), "Hello, world!")

    def test_gen_content_no_title(self):
        md = "This is a paragraph\n This is a subheading"
        with self.assertRaises(ValueError):
            extract_md(md)


if __name__ == "__main__":
    unittest.main()

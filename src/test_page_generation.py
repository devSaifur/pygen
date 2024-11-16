import unittest
from page_generation import extract_title


class TestGenContent(unittest.TestCase):
    def test_gen_content(self):
        md = "# Hello, world!\n This is a paragraph. \n\n"
        self.assertEqual(extract_title(md), "Hello, world!")

    def test_gen_content_no_title(self):
        md = "This is a paragraph\n This is a subheading"
        with self.assertRaises(ValueError):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()

import unittest

from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
        
    def test_extract_title(self):
        text = "# Hello"
        res = extract_title(text)
        self.assertEqual("Hello", res)
    
    def test_extract_title2(self):
        text = """# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter"""
        res = extract_title(text)
        self.assertEqual("Tolkien Fan Club", res)
        

    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

* and
* a
* list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass


if __name__ == "__main__":
    unittest.main()
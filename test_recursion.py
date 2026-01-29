import unittest
from Recursion import reverserString

class test_Recursion(unittest.TestCase):
    # normal edge cases
    def test_case1(self):
        assert reverserString("mom") == "mom"

    def test_case2(self):
        assert reverserString("swims") == "smiws"

    def test_case3(self):
        assert reverserString("HeLlO") == "olleh"

    ## edge cases

    def test_edge1(self):
        assert reverserString("Hello world") == "dlrow olleh"

    def test_edge2(self):
        assert reverserString("Hello world!") == "!dlrow olleh"

    def test_edge3(self):
        assert reverserString("12345") == "54321"

    def test_edge4(self):
        assert reverserString("aibohpoiladeppiuqsesortsnomotopoppih") == "hippopotomonstrosesquippedaliophobia"

    def test_edge5(self):
        assert reverserString("") == ""
    
    def test_edge6(self):
        assert reverserString("a") == "a"

    def test_edge7(self):
        assert reverserString("!@#$%") == "%$#@!"

if __name__ == "__main__":
    unittest.main()
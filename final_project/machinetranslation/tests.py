import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(englishToFrench(""),"")

    def test_hello_bonjour(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(frenchToEnglish(""),"")
    
    def test_bonjour_hello(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main()
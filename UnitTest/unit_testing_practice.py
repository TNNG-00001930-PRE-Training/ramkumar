import unittest


def concatenation(str1,str2):
    return str1+str2

def slicing(str,start,end):
    return str[start:end]

def formatting(name):
    return "My name is {}".format(name)

def uppercase(str):
    return str.upper()

def lowercase(str):
    return str.lower()


class TestCases(unittest.TestCase):

    def test_concatenation(self):
        result = concatenation("Hello ", "world")
        self.assertEqual(result, "Hello world")

    def test_slicing(self):
        result = slicing("Hello",1,3)
        self.assertEqual(result, "el")

    def test_formatting(self):
        result = formatting("Ram")
        self.assertEqual(result, "My name is Ram")

    def test_uppercase(self):
        result = uppercase("Ram")
        self.assertEqual(result, "RAM")

    def test_lowercase(self):
        result = lowercase("RAM")
        self.assertEqual(result, "ram")

        
if __name__ == '__main__':
    unittest.main()

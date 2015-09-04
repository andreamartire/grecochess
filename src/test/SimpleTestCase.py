import unittest


class SimpleTestCase(unittest.TestCase):

    def testBlah(self):
        assert "blah" == "blah", "blah isn't blahing blahing correctly"


if __name__ == "__main__":
    unittest.main() # run all tests
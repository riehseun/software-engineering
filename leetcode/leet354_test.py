import unittest

from leet354 import Leet354


class TestLeet354(unittest.TestCase):
    def setUp(self):
        self.leet354 = Leet354()

    def test_max_envelopes_1(self):
        test = self.leet354.max_envelopes([[5,4],[6,4],[6,7],[2,3]])
        self.assertEqual(test, 3)

    def test_max_envelopes_2(self):
        test = self.leet354.max_envelopes([[1,1],[1,1],[1,1]])
        self.assertEqual(test, 1)

    def test_max_envelopes_3(self):
        test = self.leet354.max_envelopes([[30,50],[12,2],[3,4],[12,15]])
        self.assertEqual(test, 3)

    def test_max_envelopes_4(self):
        test = self.leet354.max_envelopes([[51,51],[51,70],[60,60],[70,70],[1,100]])
        self.assertEqual(test, 3)

    def test_max_envelopes_5(self):
        test = self.leet354.max_envelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]])
        self.assertEqual(test, 3)

    def test_max_envelopes_6(self):
        test = self.leet354.max_envelopes([[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]])
        self.assertEqual(test, 7)


if __name__ == "__main__":
    unittest.main()

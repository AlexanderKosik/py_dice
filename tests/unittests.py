import unittest
from collections import Counter
from probabilities import probs

class TestProbabilities(unittest.TestCase):
    def test_pasch(self):
        prob, gains_6er = probs.pasch("666433", 3)
        self.assertEqual(prob, 100)
        self.assertEqual(gains_6er, 28.5)

        prob, gains_5er = probs.pasch("555433", 3)
        self.assertEqual(prob, 100)
        self.assertEqual(gains_5er, 25.5)

    def test_kniffel(self):
        prob, gain = probs.kniffel("666633")
        print(prob, gain)

if __name__ == '__main__':
    unittest.main()

import unittest

import sys
sys.path.append("../")
from probabilities import probs

class TestProbabilities(unittest.TestCase):
    def test_pasch(self):
        prob, gains_6er = probs.pasch("66643", 3)
        self.assertEqual(prob, 1)
        self.assertEqual(gains_6er, 25)

        prob, gains_5er = probs.pasch("55543", 3)
        self.assertEqual(prob, 1)
        self.assertEqual(gains_5er, 22)

    def test_kniffel(self):
        prob, gain = probs.kniffel("66633")
        self.assertEqual(round(prob, 3), 0.056)

    def test_kl_strasse(self):
        prob, gain = probs.kl_strasse("12334")
        self.assertAlmostEqual(prob, 1/3)
        self.assertEqual(gain, 30)

    def test_gr_strasse(self):
        prob, gain = probs.gr_strasse("12343")
        self.assertAlmostEqual(prob, 1/6)
        self.assertEqual(gain, 40)

        prob, gain = probs.gr_strasse("12333")
        self.assertAlmostEqual(prob, 1/18)


if __name__ == '__main__':
    unittest.main()

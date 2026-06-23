import unittest
from core.engine import MuseEngine

class TestMuseEngine(unittest.TestCase):
    def setUp(self):
        self.engine = MuseEngine()

    def test_clean_multiplicative_chain(self):
        scores = {"node_1": 1.0, "node_2": 0.9, "node_3": 0.8}
        result = self.engine.calculate_effective_integrity(scores)
        self.assertEqual(result, 0.72)

    def test_single_point_of_failure(self):
        scores = {"node_1": 1.0, "node_2": 0.0, "node_3": 0.95}
        result = self.engine.calculate_effective_integrity(scores)
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()

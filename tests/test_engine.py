import unittest
from core.engine import MuseEngine

class TestMuseEngineSimulation(unittest.TestCase):
    def setUp(self):
        self.engine = MuseEngine()

    def test_clean_pipeline_execution(self):
        """Simulates a healthy, fully compliant cross-border funding pipeline."""
        scores = {
            "node_1_treasury": 1.0, 
            "node_2_procurement": 0.9, 
            "node_3_execution": 0.85, 
            "node_4_impact": 1.0
        }
        result = self.engine.calculate_effective_integrity(scores)
        self.assertEqual(result, 0.765)

    def test_absolute_zero_systemic_collapse(self):
        """CRITICAL: Proves that a single node failure collapses the entire pipeline to 0."""
        scores = {
            "node_1_treasury": 1.0, 
            "node_2_procurement": 0.9, 
            "node_3_execution": 0.85, 
            "node_4_impact": 0.0  # Total failure at the final audit
        }
        result = self.engine.calculate_effective_integrity(scores)
        self.assertEqual(result, 0.0)

    def test_fraudulent_inflation_rejection(self):
        """Proves the engine strictly rejects inflated scores above 1.0."""
        scores = {"node_1_treasury": 1.0, "node_2_procurement": 1.5}
        with self.assertRaises(ValueError):
            self.engine.calculate_effective_integrity(scores)

    def test_negative_value_rejection(self):
        """Proves the engine strictly rejects corrupted negative inputs."""
        scores = {"node_1_treasury": 1.0, "node_2_procurement": -0.1}
        with self.assertRaises(ValueError):
            self.engine.calculate_effective_integrity(scores)

if __name__ == '__main__':
    unittest.main()

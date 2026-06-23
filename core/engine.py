# -*- coding: utf-8 -*-
"""
SENTRY-13 / MUSE v3.2 Core Multiplicative Engine
Copyright 2026 The Sumalinog Institute
Licensed under the Apache License 2.0
"""

class MuseEngine:
    def __init__(self, node_weights=None):
        """
        Initializes the calculation matrix. Node weights default to 1.0 if unassigned.
        """
        self.node_weights = node_weights if node_weights else {}

    def calculate_effective_integrity(self, node_scores):
        """
        Executes the foundational MUSE v3.2 Multiplicative Chain calculation.
        node_scores: Dict[str, float] -> Expected values between 0.0 and 1.0
        Returns: float -> Systemic integrity score
        """
        if not node_scores:
            return 0.0
            
        effective_integrity = 1.0
        
        for node_id, score in node_scores.items():
            # Validate bounding parameters
            bounded_score = max(0.0, min(1.0, score))
            effective_integrity *= bounded_score
            
        return round(effective_integrity, 6)

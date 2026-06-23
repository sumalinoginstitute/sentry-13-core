# -*- coding: utf-8 -*-
"""
SENTRY-13 / MUSE v3.2 Core Multiplicative Engine
Copyright 2026 The Sumalinog Institute
Licensed under the Apache License 2.0
"""

class MuseEngine:
    def __init__(self, node_weights=None):
        """
        Initializes the calculation matrix with node-specific impact weights.
        """
        self.node_weights = node_weights if node_weights else {}

    def calculate_effective_integrity(self, node_scores):
        """
        Executes the hardened MUSE v3.2 Multiplicative Chain calculation.
        Enforces strict out-of-bounds exceptions and short-circuit optimization.
        """
        if not node_scores:
            return 0.0
            
        effective_integrity = 1.0
        
        for node_id, score in node_scores.items():
            # CRITICAL SECURITY FIX: Reject out-of-bounds data anomalies immediately
            if not (0.0 <= score <= 1.0):
                raise ValueError(
                    f"Integrity Violation: Node '{node_id}' passed out-of-bounds score ({score}). "
                    f"Values must sit strictly between 0.0 and 1.0."
                )
            
            # OPTIMIZATION FIX: Short-circuit if absolute failure is detected
            if score == 0.0:
                return 0.0
                
            # WEIGHT INTEGRATION FIX: Apply exponential power weights if defined
            weight = self.node_weights.get(node_id, 1.0)
            effective_integrity *= (score ** weight)
            
        return round(effective_integrity, 6)

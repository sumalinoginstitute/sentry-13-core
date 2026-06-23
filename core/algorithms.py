# -*- coding: utf-8 -*-
"""
SENTRY-13 Predictive Risk Algorithms
Copyright 2026 The Sumalinog Institute
Licensed under the Apache License 2.0
"""

def evaluate_hardware_root_trust(signature_valid, key_status):
    """
    Evaluates cryptographic node identity signature derived from Nitrokey 3 tokens.
    Returns a fractional node value between 0.0 and 1.0.
    """
    if not signature_valid:
        return 0.0
    if key_status == "REVOKED":
        return 0.0
    if key_status == "VERIFIED":
        return 1.0
    return 0.5

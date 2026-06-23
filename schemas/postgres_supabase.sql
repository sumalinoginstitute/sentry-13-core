-- SENTRY-13 Hardened Database Core Schema
-- Target Environment: PostgreSQL / Supabase
-- Copyright 2026 The Sumalinog Institute

CREATE TABLE IF NOT EXISTS pipeline_nodes (
    node_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    node_name VARCHAR(255) NOT NULL,
    organization_tier VARCHAR(100) NOT NULL, -- e.g., National, Regional, Divisional
    cryptographic_root_id VARCHAR(255) UNIQUE,
    current_integrity_score NUMERIC(3, 2) CHECK (current_integrity_score >= 0.00 AND current_integrity_score <= 1.00),
    last_updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS compliance_transactions (
    transaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pipeline_id VARCHAR(100) NOT NULL,
    amount NUMERIC(15, 2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'USD',
    node_chain_snapshot JSONB NOT NULL, -- Captures active multi-node score states at time of transaction
    computed_systemic_integrity NUMERIC(7, 6) NOT NULL,
    circuit_breaker_triggered BOOLEAN DEFAULT FALSE,
    logged_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

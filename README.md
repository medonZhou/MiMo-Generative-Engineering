```markdown
# MiMo-Generative-Engineering (Generative Structural AI)

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Pydantic V2](https://img.shields.io/badge/Pydantic-V2-E92063.svg?style=flat&logo=Pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Model](https://img.shields.io/badge/LLM-Xiaomi_MiMo-FF6900.svg?style=flat)]()

An enterprise-grade, Multi-Agent orchestrated platform designed to revolutionize Automotive Electronic Structural Design (Radar & ADAS Cameras) using the Xiaomi MiMo Large Language Model.

## System Architecture

The platform transitions structural engineering from a reactive, manual iterative process to an AI-Native, deterministic generative workflow. It leverages complex **Long-Chain Reasoning** and **Multi-Agent Self-Play** to resolve multi-physics constraints (Thermal vs. EMC).

### Data Ingestion Protocol
To ensure strict cross-platform compatibility and prevent data degradation during multi-agent analysis, the system mandates the ingestion of complex multi-part models exclusively as **Single STP (STEP) Files**. The `CAD-Sync Agent` guarantees unified geometric parsing.

### Core Agent Topologies
1.  **Standard-Auditor Agent**: Executes high-dimensional RAG against AEC-Q100, ISO 26262, and OEM-specific compliance documents.
2.  **Constraint-Solver Agent**: Utilizes Chain-of-Thought (CoT) to balance conflicting variables (e.g., thermal dissipation requirements vs. radar wave transmittance).
3.  **Digital-Twin Orchestrator**: Manages state transitions and asynchronous API calls.

## Token Consumption Mechanics

This architecture relies heavily on context-rich, multi-turn reasoning. Analyzing a single automotive radar housing assembly involves:
*   Injecting 50+ pages of non-structured thermal/EMC specifications into the context window.
*   Generating 10+ rounds of automated Agent-to-Agent debate to refine design parameters.
*   **Estimated Cost:** ~30k - 80k Tokens per complete assembly audit.

A high-quota MiMo token allocation is critical to sustain the autonomous generative loops required for production-level engineering outputs.

## Quick Start
```bash
pip install -r requirements.txt
uvicorn main:app --reload

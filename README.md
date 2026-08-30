# CHRONOS

**Frontier AI Evaluation Repository, Evidence Archive & Methodology — TamilOps**

## Overview

Project CHRONOS is an independent research project developing a transparent methodology for evaluating frontier AI systems using preserved evidence, structured fact extraction, and evidence-backed reporting.

This repository serves as the public evidence archive and methodology documentation for the project. Every evaluation preserves the original evidence before separating fact extraction and reporting into independent layers, allowing other researchers to inspect, challenge, reproduce, and build upon the published work.

## The Three-Layer Evidence Model

All evaluations within this repository strictly adhere to the CHRONOS v0.1 frozen methodology:

* **Layer 1 (Immutable):** Raw, preserved evidence (e.g., timestamped screenshots, execution traces, unmodified logs). Zero interpretation.
* **Layer 2 (Fact Extraction):** Rigid extraction of Confirmed Facts, Inferred Facts, and Disputed Items directly from Layer 1. Includes strict artifact logging.
* **Layer 3 (Reporting):** The final evaluation report and downstream analysis.

## Repository Structure

* `/specimens/` — Contains the individual evaluation specifications including their respective Layer 1, 2, and 3 documents.
* `/methodology/` — Core operational frameworks, testing protocols, and systemic rules engines (including the TamilOps Evaluation Methodology).
* `/assets/` — Shared repository assets (logos, diagrams, images, and other resources used across the CHRONOS project).

## Current Evaluation Specimens

* **[SPEC-001](specimens/SPEC-001/):** Tamil Siledai Reasoning Failure & Unsupported Generated Claims
* **[SPEC-002](specimens/SPEC-002/):** Date Cascade Failure & Temporal Self-Correction
* **[SPEC-003](specimens/SPEC-003/):** Business Directory Hallucination & Self-Correction Behaviour
* **[SPEC-004](specimens/SPEC-004/):** Workflow Duplication and Transition-Control Failure

## Provenance

**Lab:** TamilOps Frontier AI Evaluation Lab
**Lead Architect:** Sirajudeen Seethapathy

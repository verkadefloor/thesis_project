# Optimising Legal Information Retrieval and Decision Support for Municipal Governance: A Modular Hybrid Split-RAG Architecture for the Dutch Omgevingswet

This repository contains the research, experiments, and implementation of a modular Retrieval-Augmented Generation (RAG) framework designed to support legal decision-making in the context of the Dutch Omgevingswet.

The research investigates whether a Split-RAG architecture can improve legal information retrieval and support the generation of case-specific legal justifications by combining statutory provisions with relevant jurisprudence. The proposed approach separates legislation and case law into dedicated retrieval channels, reducing the risk that concise statutory provisions are overshadowed by voluminous judicial rulings when indexed within a single vector space.

The framework was evaluated against a unified structure aware RAG baseline using both automated RAGAs metrics and expert assessments conducted by municipal legal experts. The results show that Split-RAG improves retrieval recall, source traceability, and answer faithfulness, while highlighting the remaining challenges of normative legal reasoning in legal AI systems.

## Project Structure
* **data/**: Contains statutory legislation and judicial jurisprudence datasets in JSONL format, the Gold Standard evaluation set (10 manually curated and expert-validated question-answer pairs), vector stores, and RAGAs evaluation results.
* **EDA/**: Contains exploratory data analysis notebook examining document characteristics such as document length, vocabulary distributions, and structural complexity.
* **expert_evaluations/**: Contains the results and analysis of expert assessments comparing the baseline and Split-RAG architecture.
* **split_rag/**: Contains the final Split-RAG implementation and supporting experimental notebook.
* **baseline/**: Contains the baseline implementation and experimental results.

## Research Objective
The primary objective of this research is to evaluate whether a modular Split-RAG architecture can improve legal information retrieval and support legal decision-making under the Dutch Omgevingswet. By separating legislation and jurisprudence into dedicated retrieval channels, the architecture aims to mitigate statutory dilution, improve source attribution, and increase the transparency and verifiability of generated legal responses.

## Technical Configuration
The system was implemented using the following specifications:
* **LLM**: GPT-4o (temperature 0.0)
* **Architecture Split-RAG**: Hybrid Split-RAG with PDR (Parent Document Retrieval) and MMR (Maximum Marginal Relevance).
* **Architecture baseline**: Structure-aware chunking.
* **Evaluation**: RAGAs frameork and expert validation.

## Setup Instructions

1. Ensure a `.env` file is present in the root directory containing valid azure variables.
2. Synchronize the environment and install the project along with all locked dependencies:
   ```bash
   uv sync



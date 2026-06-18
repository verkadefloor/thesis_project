# Legal Decision Support with Split-RAG: Omgevingswet Case Study

This repository contains the research and implementation of a modular Retrieval-Augmented Generation (RAG) framework designed to support legal decision-making within the Municipality of Amsterdam concerning the *Omgevingswet*. 

The research addresses the reasoning gap in municipal legal practice: legal experts require more than just the retrieval of relevant case law. They require a system capable of generating **dossier-specific normative justifications**, synthesizing statutory provisions from the *Omgevingswet* with relevant jurisprudence to substantiate legal advice for concrete administrative cases.
## Project Structure

* **data/**: Contains the two primary datasets—statutory legislation (JSONL) and judicial jurisprudence (JSONL). This directory also includes the Golden Standard evaluation set, consisting of 10 manually curated and expert-checked Query-Answer pairs.
* **EDA/**: Contains the Exploratory Data Analysis notebook. This includes statistical analysis of document lengths, word distributions, and syntactic complexity which justify the choice for a modular architecture.
* **data/**: Contains the datasets for statutory legislation and judicial jurisprudence, alongside the Gold Standard evaluation set (10 manually curated, expert-checked Query-Answer pairs), the vector stores and the results of the RAGAs evaluations.
* **expert_evaluations/**: Contains analysis of the data provided by legal experts concerning the baseline and Split-RAG.
* **split_rag/**: Contains the final model of the split-RAG and a notebook with experiments regarding the split-RAG.
* **baseline/**: Contains the baseline experiments.

## Research Objective

The primary objective is to evaluate whether a modular Split-RAG architecture can bridge the gap between abstract legal retrieval and actionable, case-specific decision support. By decoupling legislation and jurisprudence into dedicated channels, the architecture mitigates "semantic dilution"—where concise statutory provisions are overshadowed by voluminous judicial narratives—to generate legally defensible and verifiable justifications.

## Technical Configuration

The system is implemented using the following specifications:
* **LLM**: GPT-4o (temperature 0.0)
* **Architecture Split-RAG**: Hybrid Split-RAG with PDR (Parent Document Retrieval) and MMR (Maximum Marginal Relevance).
* **Architecture baseline**: structure-aware chunking.
* **Evaluation**: RAGAs framework and expert validation

## Setup Instructions

1. Ensure a `.env` file is present in the root directory containing valid azure variables.
2. Install the project and its dependencies:
   ```bash
   pip install -e .
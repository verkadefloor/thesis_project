# Legal Decision Support with Split-RAG: Omgevingswet Case Study

This repository contains the research and implementation of a modular Retrieval-Augmented Generation (RAG) framework designed for legal decision support within the Municipality of Amsterdam. The study focuses on the "Omgevingswet" and evaluates the performance of specialized retrieval architectures.

## Project Structure

* **data/**: Contains the two primary datasets—statutory legislation (JSONL) and judicial jurisprudence (JSONL). This directory also includes the Golden Standard evaluation set, consisting of 10 manually curated and expert-checked Query-Answer pairs.
* **EDA/**: Contains the Exploratory Data Analysis notebook. This includes statistical analysis of document lengths, word distributions, and syntactic complexity which justify the choice for a modular architecture.
* **RAGAs/**: Contains the implementation of the Retrieval Augmented Generation Assessment framework. The notebook demonstrates the methodology for calculating Faithfulness, Answer Correctness, Context Precision, and Context Recall.

## Research Objective

The primary objective of this research is to assess whether a Split-RAG architecture outperforms a traditional Naive RAG baseline. By utilizing separate vector indices for legislation and case law, the model aims to mitigate semantic drowning, a phenomenon where concise statutory articles are overshadowed by the significantly larger volume of text found in judicial rulings.

## Technical Configuration

The system is implemented using the following specifications:
* **LLM**: GPT-4o (temperature 0.0)
* **Embeddings**: not sure yet
* **Evaluation**: RAGAs framework

## Setup Instructions

1. Ensure a `.env` file is present in the root directory containing valid azure variables.
2. Install the project and its dependencies:
   ```bash
   pip install -e .
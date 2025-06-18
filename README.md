# Source-Code-summarization
This repository contains the implementation and experimentation of a source code summarization system.
Design and Analysis of Source Code Summarizer
This repository contains the implementation and experimentation of a source code summarization system.

# Project Highlights
**Objective**: To automatically generate human-readable summaries of source code using a combination of Abstract Syntax Tree (AST), Transformer, and Tree-LSTM models.

**Motivation: Simplify code understanding for developers, especially for code maintenance, modernization, and migration across languages.**

# Approach:

Integration of structural (AST-based) and semantic analysis for improved summarization.

**Experimentation with multiple models**: PLBART, CoTexT, CodeTrans, ProphetNet.

Development of a hybrid model combining Transformer and Tree-LSTM for better results.

**Cross-language Evaluation**: Model trained on Python and validated on Java and PHP for robustness.

**Dataset Used**: CodeSearchNet, enriched with StackOverflow and bug report code samples.

# 📊 Evaluation
**Metrics**: BLEU, ROUGE, METEOR, WER, LEPOR.

**Best BLEU Score**: 12.42 (after extensive training and dataset augmentation).

# 📁 Folder Structure
/models/ – Implementation of baseline and proposed models.

/data/ – Scripts for data preprocessing, AST generation, and CFG extraction.

/experiments/ – Notebooks and logs of evaluation across models and datasets.

👨‍💻 Technologies Used
Python, PyTorch

Transformer Models (PLBART, CoTexT)

Tree-LSTM

NLP Tools: SentencePiece, NLTK, Scikit-learn

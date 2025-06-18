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

**Best BLEU Score**: 35.42 (after extensive training and dataset augmentation).

# 📁 Folder Structure
/Code/ - contains code file for running.

/dataset/ – Scripts for data preprocessing and raw dtaset file in text format.

/datasetAST/ - scripts for ast and cfg and dataset converetd to AST format.

/models/ – Implementation of baseline and proposed models.

/models Already/ - Atttention, encoder-decoder, other LLM and Transformer models.

/Evaluator/ - Code for evaluation and getting bleu score.

/experiments/ – Notebooks and logs of evaluation across models and datasets.

# 👨‍💻 Technologies Used
Python, PyTorch

Transformer Models (PLBART, CoTexT)

Tree-LSTM, LLM

**NLP Tools**: SentencePiece, NLTK, Scikit-learn


# How to Run?

Install all the required libraries and dependencies.

First go to dataset folder preprocess the dataset.

then go to DatasetAST Conver dataset into ast and cfg.

Use pretrained model and finetune it.

Then Run run.py file in model / evaluator folder.

# OUTPUT
<p align="center">
  <img src="OUPUT_IMAGES/reference summaries.png" width="600"/>
  <br><i>Figure: Reference Summaries</i>
</p>

<p align="center">
  <img src="OUPUT_IMAGES/output summaries.png" width="600"/>
  <br><i>Figure:Generated Summaries</i>
</p>

<p align="center">
  <img src="OUPUT_IMAGES/Screenshot (17).png" width="600"/>
  <img src="OUPUT_IMAGES/Screenshot (19).png" width="600"/>
  <img src="OUPUT_IMAGES/Screenshot (20).png" width="600"/>
  <br><i>Figure:OUTPUT SCORE AND SUMMARY EXAMPLES</i>
</p>

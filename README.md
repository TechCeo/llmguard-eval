# LLMGuard Security Evaluation Framework

A comprehensive evaluation framework for testing **LLMGuard** across multiple LLM backends, with a focus on prompt injection detection and safe chatbot behavior.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Goals & Objectives](#goals--objectives)
- [Methodology](#methodology)
- [Experiments & Results](#experiments--results)
- [Tools & Technologies](#tools--technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results & Findings](#results--findings)
- [References](#references)

## 🎯 Project Overview

This repository evaluates **LLMGuard** by integrating it with several LLM models and measuring prompt injection detection performance.
It contains:
- `LLMGAURD_Project_notebook.ipynb` for interactive analysis and visualization,
- `llmguard_tinyllama_evaluation.py` for TinyLLaMA experiments,
- `llmguard_phi2_evaluation.py` for Microsoft Phi-2 experiments,
- `llmguard_distilgpt2_evaluation.py` for DistilGPT-2 experiments.

### Key Focus Areas
- **Prompt Injection Detection**: Identify malicious or manipulative prompt patterns.
- **Input Sanitization**: Block or sanitize unsafe prompts before model inference.
- **Cross-Model Evaluation**: Apply the same defense workflow across different LLM architectures.
- **Quantitative Metrics**: Use accuracy, precision, recall, F1-score, and confusion matrices.

## 🎓 Goals & Objectives

1. Integrate LLMGuard with TinyLLaMA, Microsoft Phi-2, and DistilGPT-2.
2. Evaluate prompt injection detection using the Safe-Guard Prompt Injection dataset.
3. Benchmark defense performance with standard classification metrics.
4. Provide a reproducible interactive notebook and experiment scripts.
5. Document the full project implementation.

## 🔬 Methodology

### Evaluation Pipeline

```
User Prompt → LLMGuard Scanner → Risk Assessment → Accept/Reject → Model Response or Block Message
```

### Dataset
- **Safe-Guard Prompt Injection** (`xTRam1/safe-guard-prompt-injection`)
  - Labels: safe (0), unsafe (1)
  - Used for both script-based and notebook evaluations.

### Models Evaluated
- TinyLLaMA-1.1B-Chat
- Microsoft Phi-2
- DistilGPT-2

### Defense Components
- PromptInjection scanner
- Prompt sanitization and blocking
- Risk scoring
- Response-level safety checks where applicable

### Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Classification report

## 🧪 Experiments & Results

### Experiment 1: TinyLLaMA-1.1B-Chat
**File**: `llmguard_tinyllama_evaluation.py`

This script evaluates the TinyLLaMA defense pipeline and shows how LLMGuard blocks dangerous prompts while allowing safe inputs.

### Experiment 2: Microsoft Phi-2
**File**: `llmguard_phi2_evaluation.py`

This script validates the same defense design with Microsoft Phi-2.

### Experiment 3: DistilGPT-2
**File**: `llmguard_distilgpt2_evaluation.py`

This script evaluates DistilGPT-2 and includes optional GPT4All-local experiment scaffolding.

### Interactive Notebook
**File**: `LLMGAURD_Project_notebook.ipynb`

The notebook provides an interactive walkthrough of:
- TinyLLaMA model loading,
- LLMGuard scanner usage,
- manual prompt injection tests,
- dataset-based evaluation,
- metrics and visualizations,
- false negative analysis.

### Attack Patterns Tested
- Instruction override prompts
- Roleplay injection prompts
- Malicious payload prompts
- Context confusion prompts

## 🛠 Tools & Technologies

- `llm-guard`
- `transformers`
- `torch`
- `datasets`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

## 📁 Project Structure

```
llmguard-eval/
├── README.md
├── LLMGAURD_Project_notebook.ipynb
├── llmguard_tinyllama_evaluation.py
├── llmguard_phi2_evaluation.py
├── llmguard_distilgpt2_evaluation.py
└── requirements.txt
```

## 💾 Installation

### Prerequisites
- Python 3.8 or higher
- CUDA 11.8+ (optional)
- 8GB+ RAM recommended



### Optional
For optional local GPT4All experiments in `llmguard_distilgpt2_evaluation.py`:

```bash
pip install gpt4all
```

## 🚀 Usage

### Run scripts

```bash
python llmguard_tinyllama_evaluation.py
python llmguard_phi2_evaluation.py
python llmguard_distilgpt2_evaluation.py
```

### Run the notebook

Open `LLMGAURD_Project_notebook.ipynb` in Jupyter, JupyterLab, or GitHub's notebook viewer and run the cells sequentially.

## 📊 Results & Findings

This project demonstrates how LLMGuard can be applied across multiple LLM architectures and evaluated with prompt injection datasets. The notebook provides interactive evidence and visualization of the defense pipeline.

## 📚 References

- `xTRam1/safe-guard-prompt-injection`
- `TinyLLaMA/TinyLLaMA-1.1B-Chat-v1.0`
- `microsoft/phi-2`
- `distilgpt2`
- `protectai/llm-guard`

## 📄 License

Research and educational use only. Refer to dependency licenses.

## 👤 Author

**Yusuf Adamu**

# LLM from Scratch – GPT-2 Implementation

## 📌 Overview
This repository contains a **from-scratch implementation of the GPT-2 architecture**, including **pretraining and fine-tuning** stages.  
The project focuses on understanding the **internal mechanics of large language models (LLMs)** rather than relying on high-level frameworks.

The implementation covers:
- Transformer decoder architecture
- Tokenization and embeddings
- Self-attention and feed-forward layers
- Pretraining on raw text
- Fine-tuning for downstream tasks

## 🎯 Objectives
- Build GPT-2 architecture from first principles
- Understand transformer internals at code level
- Pretrain an LLM on textual data
- Fine-tune the model for task-specific adaptation
- Analyze training stability and convergence

## 🧠 Model Architecture
The model is based on the **GPT-2 (decoder-only Transformer)** architecture, consisting of:
- Token embedding + positional embedding
- Multi-head self-attention
- Layer normalization (Pre-Norm)
- Feed-forward neural networks
- Residual connections

## 🏗️ Project Scope
- Custom GPT-2 implementation (no pretrained weights)
- Training loop implementation
- Pretraining from random initialization
- Fine-tuning pipeline
- Text generation inference

> ⚠️ This project is educational and research-oriented, not optimized for production deployment.

## 🛠️ Tech Stack
- **Python**
- **PyTorch**
- **NumPy**
- **Tokenization utilities**
- **CUDA (optional, for acceleration)**

## 📂 Repository Structure
LLM-from-Scratch/
├── model/ # GPT-2 architecture implementation
├── tokenizer/ # Tokenization logic
├── train.py # Pretraining script
├── finetune.py # Fine-tuning script
├── inference.py # Text generation
├── requirements.txt
├── README.md


## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/PrasannaMadiwar/LLM-from-Scratch-.git
cd LLM-from-Scratch-
2️⃣ Install dependencies
pip install -r requirements.txt
```

## 🚀 Training Workflow
🔹 Pretraining
- Pretraining is performed from randomly initialized weights using unlabeled text data.
- python train.py

## 🔹 Fine-Tuning

Fine-tuning adapts the pretrained model to a task-specific dataset.

python finetune.py

## 🔹 Text Generation
python inference.py

## 📊 Key Learnings

Transformer attention mechanics

Training stability in deep LLMs

Tokenization impact on language modeling

Pretraining vs fine-tuning dynamics

Memory and compute trade-offs in LLMs

## 🚀 Future Improvements

Implement mixed-precision training

Add distributed training support

Optimize attention computation

Scale to larger GPT variants

Evaluate on benchmark NLP tasks

## 📖 References

Attention Is All You Need — Vaswani et al.

Language Models are Unsupervised Multitask Learners — Radford et al.

PyTorch Documentation

## 👤 Author

Prasanna Madiwar
AI/ML Engineering Intern Aspirant
GitHub: https://github.com/PrasannaMadiwar

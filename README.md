# YouTube RAG Chatbot 🎥🤖

A **Retrieval-Augmented Generation (RAG) based conversational chatbot** that allows users to ask questions about **YouTube videos** using their transcripts. The system dynamically extracts video transcripts, builds a semantic index, and generates **grounded, context-aware answers** using Large Language Models (LLMs).

---

## 🚀 Project Overview

YouTube is a powerful learning platform, but extracting specific information from long videos or lectures is time-consuming. This project transforms **unstructured video content into a conversational, searchable knowledge base**, enabling users to interactively query video content instead of passively consuming it.

---

## 🧠 Key Features

- Dynamic transcript ingestion using YouTube Transcript API  
- Custom LangChain `BaseLoader` for video-based document ingestion  
- Recursive text chunking with overlap to preserve semantic continuity  
- Semantic embeddings and vector-based retrieval using FAISS  
- Retrieval-Augmented Generation to minimize hallucinations  
- Conversational Q&A with short-term memory support  
- Modular, production-grade AI backend architecture  

---

## 🏗️ System Architecture

YouTube URL
↓
Transcript Extraction (YouTube Transcript API)
↓
Custom LangChain BaseLoader → Document Objects
↓
Text Chunking (Recursive Splitter)
↓
Embedding Generation
↓
Vector Store (FAISS)
↓
ConversationalRetrievalChain
↓
LLM Response (Grounded Answer)


---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **OpenAI LLMs & Embeddings**
- **FAISS (Vector Database)**
- **YouTube Transcript API**

---

## 📁 Project Structure

├── youtube_transcript_loader.py # Custom LangChain BaseLoader
├── rag_chatbot.py # RAG pipeline + memory
├── main.py # Example usage
├── README.md


---

## 🔍 Why Retrieval-Augmented Generation (RAG)?

Instead of fine-tuning an LLM, this project uses **RAG** to keep knowledge **dynamic, explainable, and scalable**. Retrieval ensures that answers are grounded in actual video content, significantly reducing hallucinations and improving factual accuracy.

Retrieval acts as the **single source of truth**, while the LLM is responsible for reasoning and natural language generation.

---

## 🧠 Conversational Design Decisions

### ✔ Chain Selection: `ConversationalRetrievalChain`

This chain was chosen because it is specifically designed for **conversational RAG systems**. It automatically rewrites follow-up questions into standalone queries before retrieval, improving semantic search accuracy and handling conversational references like “that” or “this part.”

---

### ✔ Memory Strategy

- Uses **short-term conversation window memory (last 3–4 turns)**
- Avoids long-term summary memory to prevent abstraction drift and hallucination risk
- Keeps token usage predictable and retrieval-focused

> In this system, **retrieval—not memory—is the source of truth**. Memory is used only to improve conversational flow.

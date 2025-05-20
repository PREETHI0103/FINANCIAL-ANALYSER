# FINANCIAL-ANALYSER
# 💸 UPI Analyzer App

An intelligent personal finance tool that extracts and analyzes UPI transaction data from financial PDFs (Paytm, GPay, PhonePe, etc.) using LLMs to provide insights, summaries, and personalized financial recommendations.

---

## 🚀 Features

- ✅ Extracts structured data (Date, Time, Amount, Receiver, Description, Category) from UPI PDF statements  
- 🧹 Cleans and normalizes transaction data using `pandas`  
- 📊 Analyzes spending patterns, time-based trends, and category-wise summaries  
- 🔍 Detects wasteful/unusual transactions using LLMs  
- 🤖 Generates LLM-based recommendations:
  - Monthly budget planning
  - Spending reduction strategies
  - Personalized financial advice  
- 🌐 Deployed with Streamlit or Gradio  
- ☁️ Hostable on Hugging Face Spaces or other free-tier cloud platforms

---

---

## 📝 Step-by-Step Implementation

### 1. 📥 Dataset Preparation

- **Input:**  
  UPI PDF statements from Paytm, PhonePe, GPay, etc.

- **Output:**  
  Structured data in CSV/JSON format with fields:
  - `Date`, `Time`, `Amount`, `Receiver`, `Description`, `Category`

- **Libraries Used:**  
  - `pdfplumber` or `PyMuPDF` for parsing PDFs  
  - `pandas` for structuring data

---

### 2. 🧼 Text Preprocessing and Structuring

- Parse PDFs using `pdfplumber` or `PyMuPDF`
- Normalize and clean data:
  - Convert timestamps and numeric fields
  - Standardize column names and formats
  - Extract merchant names and transaction categories from descriptions

---

### 3. 🧠 Model Development (Langflow + LLM)

Use Langflow to build an interactive flow with chained LLM components for:

- 📊 Spending pattern analysis  
- 🕒 Time-based trends  
- 📂 Category-wise summaries  
- 🚫 Wasteful transaction detection

---

### 4. 🤖 LLM-Based Recommendation Generation

Prompt an LLM (e.g., GPT-4) for:

- 🗓 Monthly budget planning  
- ✂️ Suggestions to reduce unnecessary spending  
- 💡 Personalized financial advice based on transaction behavior

**Example Prompt:**

---

### 5. 🚀 Deployment

- **Interface:** Streamlit or Gradio  
- **Hosting Options:**
  - Hugging Face Spaces (recommended for free hosting)
  - Streamlit Community Cloud
  - Localhost

---



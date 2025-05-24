# 💰 Smart Financial Analyzer (FinAssist AI)

**FinAssist AI** is an AI-powered Streamlit web application that analyzes UPI and bank statement PDFs, extracts transaction data, and generates **personalized financial insights** using **Google Gemini 1.5 Flash**. Designed with simplicity and intelligence, it helps users understand, track, and optimize their spending habits effortlessly.

---

🔗 **Live Demo**  
[👉 Try it on Streamlit Cloud](https://financial-analyser-9wrdwpgbqxyfxam2yotrpn.streamlit.app/)

---

## 🚀 Key Features

### 📄 Upload & Extract
- Upload UPI/bank statements (PDFs from Paytm, GPay, PhonePe, SBI, ICICI, HDFC, etc.)
- PDF text extraction using `pdfplumber`

### 🤖 Gemini-Powered Transaction Extraction
- Powered by **Google Gemini 1.5 Flash**
- Extracts structured transaction data:
  - 📅 Date
  - 🕒 Time (if available)
  - 💸 Amount
  - 🧾 Description
  - 👤 Receiver
  - 📂 Category (Debit, Credit, etc.)

### 📊 AI-Generated Financial Report
- Fully Markdown-rendered and human-readable
- Report includes:
  - **Financial Overview** (Income, Expenses, Savings)
  - **Time-based Trends**
  - **Category-wise Spend Breakdown**
  - **Monthly Comparisons**
  - **Wasteful & Frequent Spending**
  - **50-30-20 Budget Advice**
  - **Personalized Money-Saving Tips**

### 📥 Export Options
- 📤 Download extracted transactions as **JSON**
- 📄 Download the full **financial report** (.txt)
- 🎉 “Balloons” animation after successful download

---

## 🧠 How It Works

1. **Upload PDF** (e.g., GPay, Paytm, or Bank Statement)
2. **Text extracted** via `pdfplumber`
3. **Sent to Gemini AI**
4. **Gemini extracts** all transactions → structured JSON
5. **Another Gemini call** analyzes the data and returns a detailed Markdown report
6. **Displayed in-app** + downloadable report

---

## 📦 Tech Stack

| Tool / Library        | Purpose                          |
|-----------------------|----------------------------------|
| `streamlit`           | Web interface                    |
| `pdfplumber`          | PDF text extraction              |
| `google.generativeai`| Gemini 1.5 Flash API integration |
| `json`, `os`          | File handling and parsing        |
| `markdown`            | Report formatting                |

---

## 🙋 Use Cases

- 📈 Personal finance tracking  
- 💡 Budget planning & optimization  
- 🧾 Automated expense analysis  
- 🔍 Detecting wasteful spending habits  
- 💬 Financial coaching insights  

---

## 👩‍💻 Author

Built with ❤️ by **[PREETHI S]**

---


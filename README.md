💰 Smart Financial Analyzer (FinAssist AI)
An AI-powered Streamlit web application that analyzes UPI or bank statement PDFs and generates personalized financial insights using Google Gemini (Gemini 1.5 Flash). This intelligent assistant extracts transactions, detects patterns, and gives budgeting tips — all in a simple, beautiful interface.

🔗 Live Demo (Streamlit Cloud)

https://financial-analyser-9wrdwpgbqxyfxam2yotrpn.streamlit.app/

🚀 Key Features
📄 Upload & Extract
Upload bank/UPI statements (PDFs from Paytm, GPay, PhonePe, SBI, ICICI, HDFC etc.)

Text extracted using pdfplumber 🔍

🤖 Gemini-Powered Transaction Extraction
Transactions parsed using Google Gemini 1.5 Flash

Output includes:

📅 Date

🕒 Time (if available)

💸 Amount

🧾 Description

👤 Receiver

📂 Category (Debit, Credit, etc.)

📊 AI-Generated Financial Report
Fully Markdown-rendered, readable financial insights

Structured report with tables, emojis, and headings

Key sections:

Financial Overview (Income, Expenses, Savings)

Time-based Trends

Category-wise Spend Breakdown

Monthly Comparisons

Wasteful & Frequent Spending

50-30-20 Budget Advice

Personalized Money-Saving Tips

📥 Export Options
Download JSON of extracted transactions

Download full financial report (.txt)

🎉 “Balloons” animation before download to boost user delight

🧠 How It Works
Upload a PDF (e.g., GPay or bank statement)

App extracts and sends the text to Gemini AI

Gemini extracts all transactions → JSON

Another Gemini call analyzes the data and returns a detailed report

Displayed in-app and available for download

📦 Tech Stack
Tool / Library	Purpose
streamlit	Web interface
pdfplumber	PDF text extraction
google.generativeai	Gemini 1.5 Flash API integration
json & os	File handling and parsing
markdown	Report formatting

📸 Screenshots
Upload PDF	Extracted Transactions	Insights Report

You can add real screenshots of your deployed app in a screens/ folder.

⚙️ Setup Instructions
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/finassist-ai.git
cd finassist-ai
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set Gemini API key
Create a .env file:

env
Copy
Edit
GEMINI_API_KEY=your_google_generative_ai_key
Run the app locally

bash
Copy
Edit
streamlit run app.py
🌐 Deployment
Deployed on Streamlit Cloud for free access:

Just link the GitHub repo

Add the GEMINI_API_KEY in the Secrets section

The app is now accessible via a public URL

🙋 Use Cases
📈 Personal finance tracking

💡 Budget planning & optimization

🧾 Automated expense analysis

🔍 Detecting wasteful spending habits

💬 Financial coaching insights

✨ Future Improvements
Add category auto-detection using NER models or rules

Support for CSV uploads (not just PDFs)

Add charts/visualizations using Plotly or Altair

Multi-language support (for non-English statements)

🧑‍💻 Author
Built with ❤️ by [PREETHI S]


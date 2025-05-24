import os
import json
import streamlit as st
import pdfplumber
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

def extract_text(file_path):
  with pdfplumber.open(file_path) as pdf:
    return "\n".join(page.extract_text() or "" for page in pdf.pages[:]).strip()

def extract_transactions(text):
  prompt = f"""You are a financial assistant. Given this bank or UPI statement text, extract all transactions as a JSON array.

Each transaction should have:
- "Date" (YYYY-MM-DD)
- "Time" (or null)
- "Amount" (numeric)
- "Receiver" (string)
- "Description" (string)
- "Category" (e.g., Credit, Debit, Payment, Refund)

Return ONLY a valid JSON array. No extra text.

Text:
{text}
"""
  model = genai.GenerativeModel("models/gemini-1.5-flash")
  response = model.generate_content(prompt).text.strip()

  if response.startswith("```"):
    response = response.strip("`").split("json")[-1].strip()

  if not response:
    raise ValueError("Gemini returned empty response.")

  try:
    return json.loads(response)
  except Exception as e:
    raise ValueError(f"Invalid JSON from Gemini: {e}\n--- Raw Response ---\n{response}")

def generate_insights(transactions):

  prompt = f"""
You are FinAssist AI — a smart, friendly, and highly analytical personal finance assistant.

Given a user's UPI or bank transactions (JSON), generate a **comprehensive financial insights report** that is:

- Visual: Use **tables**, **headings**, **emojis**, and **bullet points**.
- Structured: Divide into **at least 10 headings/sections**.
- Simple: Avoid code blocks, or long paragraphs.
- Helpful: Include real **calculations**, **category improvement**, and **actionable tips**.

---

📥 **Input Format (JSON)**:
Each transaction contains:
- "Date"
- "Time"
- "Amount"
- "Receiver"
- "Description"
- "Category" (may be missing or labeled "Credit"/"Debit")

---

🎯 **Tasks & Report Structure** (Use headings + emojis):

---

### 📊 Financial Overview (Summary Table)
- Calculate:
  - **Total Income** (₹) — include categories like Salary, Refunds
  - **Total Expenses** (₹) — include all spend categories
  - **Net Savings** (₹) = Income − Expenses
- Present in table format:

| 💼 Metric         | Amount (₹) |
|-------------------|------------|
| 💰 Total Income   | ₹xx,xxx    |
| 💸 Total Expenses | ₹yy,yyy    |
| ✅ Net Savings    | ₹zz,zzz    |

---

### 📅 Time-Based Spending Trends
- Analyze spending patterns across:
  - Days of week
  - Time of day
  - Monthly trends
- Example bullet points:
  - 🕒 Most spending occurs on Friday evenings.
  - 📆 Highest spend month: March (₹xx,xxx)

---

### 💰Category-Wise Expense Breakdown
- Table format:

| 🏷️ Category    | Total Spent (₹) | No. of Transactions |
|----------------|------------------|----------------------|
| 🍽️ Food        | ₹xxxx            | xx                   |
| 🛍️ Shopping     | ₹xxxx            | xx                   |
| 🌍 Entertainment | ₹xxxx            | xx                   |
| ✈️ Travel       | ₹xxxx            | xx                   |
| 💰 Bills        | ₹xxxx            | xx                   |
| 💰 Salary       | ₹xxxx            | xx                   |
| 💰 Refund       | ₹xxxx            | xx                   |
| 🛒 Groceries    | ₹xxxx            | xx                   |
| 💰 Subscriptions | ₹xxxx            | xx                   |
| 📚 Education    | ₹xxxx            | xx                   |
| 📊 Others       | ₹xxxx            | xx                   |

- - Highlight any unusually high-spending categories

---

### 🔁 Monthly Comparison Summary
- Compare expense trends across months
- Table example:

| 📆 Month   | Total Spent (₹) | % Change |
|-----------|------------------|----------|
| January   | ₹xx,xxx          | -        |
| February  | ₹yy,yyy          | +8%      |

---


### 🔁 Frequent & Wasteful Spending
- Identify:
  - Frequent vendors (e.g., Swiggy, Zomato, Amazon)
  - Low-value, high-frequency transactions
- List as bullet points:
  - 🛒 18 orders from Swiggy totaling ₹4,560
  - ☕ 15 coffee shop visits totaling ₹2,100
- Suggest reduction strategies for each

---

### 📈 Monthly Budget Recommendation (50-30-20 Rule)
- Calculate recommended budget allocation:

| Budget Category     | Suggested % | Suggested Budget (₹) |
|---------------------|-------------|-----------------------|
| ✅ Needs (Essentials) | 50%         | ₹xxxxx                |
| 🎉 Wants              | 30%         | ₹xxxxx                |
| 💹 Savings            | 20%         | ₹xxxxx                |

- Based on actual spending

---

### 💡 Personalized AI Money-Saving Tips
- Use bullet points to highlight:
  - ✅ Positive habits
  - ⚠️ Risky patterns
  - 💡 Suggestions like automating savings, UPI limits, spending caps

---

### 📌 Insights Snapshot (At a Glance)
- 3–5 key takeaways using bullet points with emojis
  - 💰 Your income exceeded expenses by ₹zz,zzz — great savings!
  - 📉 Food delivery made up 22% of total spend.
  - 🕒 Friday evenings = peak spending time.

---

⚠️ **Final Notes**:
- Markdown only
- Tables for metrics, bullet points for suggestions
- NO code blocks or charts
- Keep language friendly, helpful, and visually appealing

---

📦 **User Transactions (JSON)**:
{json.dumps(transactions, indent=2)}

"""

  model = genai.GenerativeModel("models/gemini-1.5-flash")
  return model.generate_content(prompt).text.strip()

st.set_page_config(page_title="Smart Financial Analyzer", page_icon="💰")

st.sidebar.title("💡 Welcome to FinAssist AI")
st.sidebar.markdown("""
Your smart, AI-powered finance companion is here to help! 🚀

**How it works:**
1. 📄 Upload your bank/UPI statement (PDF)
2. 🤖 Let the AI analyze your transactions
3. 📊 Get personalized insights & money-saving tips!

---
""")

st.sidebar.markdown("### 💬 Feedback")
user_feedback = st.sidebar.text_area("Help us improve by sharing your thoughts:", "")
if st.sidebar.button("📩 Submit Feedback"):
  if user_feedback.strip():
    st.sidebar.success("🎉 Thank you for your feedback!")
  else:
    st.sidebar.warning("⚠️ Please enter your feedback before submitting.")

st.title("💰 Smart Financial Analyzer")
st.markdown("""
Welcome to **FinAssist AI** – your digital finance buddy!
Analyze your **bank or UPI statements** to uncover:
- Spending patterns 🧾
- Budgeting opportunities 💡
- Personalized financial advice 📌
""")

uploaded_file = st.file_uploader("📤 Upload your PDF statement", type="pdf")

if uploaded_file:
  with open("temp.pdf", "wb") as f:
    f.write(uploaded_file.read())

  text = extract_text("temp.pdf")
  os.remove("temp.pdf")

  if not text:
    st.error("❌ No readable text found in the uploaded PDF.")
  else:
    st.info("🔍 Extracting transactions from your statement...")

    try:
      transactions = extract_transactions(text)
      st.success(f"✅ Successfully extracted {len(transactions)} transactions!")

      st.download_button(label="⬇️ Download Transactions (JSON)", data=json.dumps(transactions, indent=2), file_name="transactions.json",
          mime="application/json")

      st.info("🧠 Generating financial insights...")
      report = generate_insights(transactions)

      st.markdown("### 📊 Your Personalized Financial Report")
      st.markdown(report)

      if st.button("🎉 Prepare Download with Balloons"):
        st.balloons()
        st.session_state.download_ready = True

      if st.session_state.get("download_ready"):
        st.download_button(label="⬇️ Download Financial Insights", data=report, file_name="financial_insights.txt", mime="text/plain")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
else:
    st.info("📎 Please upload a bank or UPI PDF statement to begin.")

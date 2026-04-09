# 🧠 AI-First CRM – HCP Interaction Module

## 📌 Overview

This project is an **AI-first Customer Relationship Management (CRM) system** focused on Healthcare Professionals (HCPs).
It enables users (field representatives) to log interactions with doctors using both:

* 📝 Structured Form-based entry
* 💬 Conversational AI-based entry

The system leverages **LangGraph + Groq LLM** to provide intelligent assistance such as summarization, entity extraction, and follow-up recommendations.

---

## 🚀 Key Features

### 🔹 1. Log Interaction (Form)

* Capture HCP interaction details:

  * Doctor Name
  * Interaction Type
  * Notes
  * Follow-up actions
* Data is stored in database via FastAPI

### 🔹 2. AI Chat Interface

* Users can describe interaction in natural language
* AI processes and returns:

  * Summary
  * Extracted entities (doctor, topics)
  * Suggested follow-up actions

### 🔹 3. View All Interactions

* Fetch and display all stored interactions
* REST API endpoint: `/interactions`

---

## 🤖 AI Agent (LangGraph Concept)

The system uses an **AI Agent** that orchestrates multiple tools to process user input.

### 🧠 Role of AI Agent

* Understand user input (chat or form)
* Trigger appropriate tools
* Generate structured outputs using LLM

---

## 🛠 AI Tools Implemented

1. **Log Interaction Tool**

   * Stores interaction data into database

2. **Edit Interaction Tool**

   * Updates existing interaction records

3. **Summarization Tool**

   * Converts raw notes into concise summary using LLM

4. **Entity Extraction Tool**

   * Extracts key information such as doctor name, product, and discussion topics

5. **Follow-up Suggestion Tool**

   * Suggests next actions based on interaction context

---

## 🧱 Tech Stack

### Frontend

* React.js
* Redux Toolkit
* Axios

### Backend

* FastAPI
* SQLAlchemy
* Pydantic

### AI & LLM

* LangGraph (agent flow concept)
* Groq API (gemma2-9b-it model)

### Database

* SQLite (can be replaced with MySQL/PostgreSQL)

---

## 📁 Project Structure

```
AI-CRM/
│── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── tools.py
│   │   ├── agent.py
│   │   ├── database.py
│
│── frontend/
│   ├── src/
│   ├── public/
│
│── README.md
│── .gitignore
```

---

## ⚙️ Setup Instructions

### 🔹 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

👉 Backend runs on:

```
http://127.0.0.1:8000
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

👉 Frontend runs on:

```
http://localhost:3000
```

---

## 🔐 Environment Variables

Create `.env` file inside backend:

```
GROQ_API_KEY=your_api_key_here
```

⚠️ Do not commit `.env` file to GitHub

---

## 🌐 API Endpoints

| Method | Endpoint        | Description          |
| ------ | --------------- | -------------------- |
| POST   | `/log`          | Save interaction     |
| PUT    | `/edit/{id}`    | Edit interaction     |
| GET    | `/interactions` | Get all interactions |
| POST   | `/chat`         | AI processing        |

---

## 🎥 Demo (To be recorded)

* Form-based interaction logging
* AI chat interaction
* Display of stored interactions
* Explanation of AI tools and architecture

---

## 🧠 What I Learned

* Building AI-first applications
* Integrating LLM (Groq) into real-world workflow
* Designing modular AI tools
* Backend-frontend integration
* State management using Redux

---

## 🚀 Future Improvements

* Authentication (login system)
* Dashboard analytics
* Search & filter interactions
* Multi-user support
* Cloud database integration

---

## 🙌 Conclusion

This project demonstrates how AI can enhance CRM systems by automating insights, improving productivity, and enabling smarter interaction tracking for healthcare professionals.

---

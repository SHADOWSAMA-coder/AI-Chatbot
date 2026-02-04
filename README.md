# AI Chatbot Using Large Language Models

## Project Description
This project is a full-stack AI chatbot application developed using modern Large Language Models (LLMs).  
The system allows users to interact with an AI chatbot through a web-based interface.  
The frontend is built using Streamlit, while the backend is developed using FastAPI and communicates with the Gemini LLM API to generate responses.

---

## Technology Stack
- Python
- FastAPI (Backend)
- Streamlit (Frontend)
- Google Gemini LLM API
- GitHub (Version Control)

---

## Project Structure
AI-Chatbot/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│
├── report/
│   └── AI chatbot report.pdf
│
├── README.md
├── .gitignore

---

## How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/SHADOWSAMA-coder/AI-Chatbot.git
cd AI-Chatbot
```

### Step 2: Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate    # Linux / Mac
# .venv\Scripts\activate     # Windows

pip install -r requirements.txt
uvicorn main:app --reload
```
### Step 3: Frontend setup
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

### Step 4: Enviornment Variables
create a .env file inside the backend and add your API key
```bash
GEMINI_API_KEY=your_api_key_here
```


All application screenshots, architecture diagrams, and execution results are included in project report PDF located in report/ folder
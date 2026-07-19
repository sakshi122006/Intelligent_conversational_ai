# Intelligent Conversational AI for Karnataka State Police (KSP)

KSP Crime Intelligence AI — a scaffolded starter for a full-stack, AI-powered police intelligence platform.

Tech stack
- Frontend: React (Vite), Tailwind CSS, React Router, Recharts, Leaflet
- Backend: FastAPI (Python)
- Database: Microsoft SQL Server (MSSQL)
- Vector DB: ChromaDB
- Graph DB: Neo4j
- AI: OpenAI + LangChain
- ML: Scikit-learn, XGBoost
- Auth: JWT
- PDF Export: ReportLab
- Voice: OpenAI Whisper
- Deployment: Docker + docker-compose

Quick start (development)
1. Copy .env.example to .env and fill in secrets.
2. Start services with Docker Compose:
   docker-compose up --build

This brings up MSSQL, Neo4j, ChromaDB, backend, and frontend development servers (see docker-compose.yml).

Run frontend locally
- cd frontend
- npm install
- npm run dev

Run backend locally
- cd backend
- python -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
- uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Development notes
- The backend contains API stubs and AI/DB integration scaffolds in app/ai and app/database.
- The database/schema.sql provides a minimal schema for FIRs, crimes, users, audit logs, and chat_history.
- Fill in real secrets and production settings before deploying. Use strong JWT secret and MSSQL SA password.

License: Add your license.

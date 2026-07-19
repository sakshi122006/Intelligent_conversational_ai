from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="KSP Crime Intelligence API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# simple health
@app.get("/health")
async def health():
    return {"status": "ok"}

# Mount routers (placeholders)
from app.api import auth, chatbot, crimes
app.include_router(auth.router, prefix="/api/auth")
app.include_router(chatbot.router, prefix="/api/chatbot")
app.include_router(crimes.router, prefix="/api/crimes")

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from backend.llm_client import LLMClient
import os

app = FastAPI(title="CKD Prediction System")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (if any)
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "../static")), name="static")

# Serve frontend at root
@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(os.path.dirname(__file__), "../frontend/index.html"))

# Initialize LLM client
llm_client = LLMClient()

class PatientData(BaseModel):
    age: int = Field(..., ge=0, le=120)
    blood_pressure: int = Field(..., ge=60, le=250)
    specific_gravity: float = Field(..., ge=1.0, le=1.05)
    albumin: int = Field(..., ge=0, le=5)
    sugar: int = Field(..., ge=0, le=5)
    red_blood_cells: str = Field(..., pattern="^(normal|abnormal)$")
    pus_cell: str = Field(..., pattern="^(normal|abnormal)$")
    pus_cell_clumps: str = Field(..., pattern="^(present|notpresent)$")
    bacteria: str = Field(..., pattern="^(present|notpresent)$")
    blood_glucose_random: int = Field(..., ge=0, le=500)
    blood_urea: int = Field(..., ge=0, le=200)
    serum_creatinine: float = Field(..., ge=0.0, le=20.0)
    sodium: int = Field(..., ge=0, le=200)
    potassium: float = Field(..., ge=0.0, le=20.0)
    hemoglobin: float = Field(..., ge=0.0, le=20.0)
    packed_cell_volume: int = Field(..., ge=0, le=100)
    white_blood_cell_count: int = Field(..., ge=0, le=20000)
    red_blood_cell_count: float = Field(..., ge=0.0, le=10.0)
    hypertension: str = Field(..., pattern="^(yes|no)$")
    diabetes_mellitus: str = Field(..., pattern="^(yes|no)$")
    coronary_artery_disease: str = Field(..., pattern="^(yes|no)$")
    appetite: str = Field(..., pattern="^(good|poor)$")
    pedal_edema: str = Field(..., pattern="^(yes|no)$")
    anemia: str = Field(..., pattern="^(yes|no)$")

class PredictionRequest(BaseModel):
    data: Dict[str, Any]

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/predict")
async def predict(request: PredictionRequest):
    """Predict CKD probability using LLM"""
    try:
        prediction = llm_client.predict(request.data)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
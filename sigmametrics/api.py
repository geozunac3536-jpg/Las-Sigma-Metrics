from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .core import re_q_score

app = FastAPI(title="Sigma-Metrics API")

class Metrics(BaseModel):
    t: List[float]
    R: List[float]
    LI: List[float]
    RMSE_SL: List[float]
    kappaSigma: List[float]

class Score(BaseModel):
    score: List[float]
    max_score: float

@app.post("/score", response_model=Score)
def score(m: Metrics):
    score, mx = re_q_score(m.R, m.LI, m.RMSE_SL)
    return {"score": score, "max_score": mx}

from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI(title="Batch Sentiment Analysis API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

analyzer = SentimentIntensityAnalyzer()


class SentimentRequest(BaseModel):
    sentences: List[str] = Field(..., min_length=1)


@app.get("/")
def root():
    return {
        "message": "Batch Sentiment Analysis API is running",
        "endpoint": "POST /sentiment",
    }


@app.post("/sentiment")
def analyze_sentiment(payload: SentimentRequest):
    results = []
    for sentence in payload.sentences:
        compound = analyzer.polarity_scores(sentence)["compound"]
        if compound >= 0.05:
            label = "happy"
        elif compound <= -0.05:
            label = "sad"
        else:
            label = "neutral"
        results.append({"sentence": sentence, "sentiment": label})
    return {"results": results}

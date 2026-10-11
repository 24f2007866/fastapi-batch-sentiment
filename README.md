# FastAPI Batch Sentiment Analysis

A small FastAPI service for the batch sentiment assignment.

## Endpoint

`POST /sentiment`

Request JSON:
```json
{
  "sentences": [
    "I love this product!",
    "This is terrible.",
    "The meeting is at 3 PM."
  ]
}
```

Response JSON:
```json
{
  "results": [
    {"sentence": "I love this product!", "sentiment": "happy"},
    {"sentence": "This is terrible.", "sentiment": "sad"},
    {"sentence": "The meeting is at 3 PM.", "sentiment": "neutral"}
  ]
}
```

## Deploy on Vercel

1. Create a new GitHub repository and upload `app.py`, `requirements.txt`, and this README to its root.
2. In Vercel, choose **Add New → Project**, import that repository, and deploy. Vercel supports FastAPI apps at recognized entry points such as root-level `app.py`.
3. When deployment finishes, copy the production domain, for example `https://your-project.vercel.app`.
4. Submit `https://your-project.vercel.app/sentiment` as the FastAPI URL.
5. Test using the interactive docs at `https://your-project.vercel.app/docs`; choose `POST /sentiment`, click **Try it out**, paste the example JSON, and execute.

Do not submit the example domain; use the actual domain shown by Vercel.

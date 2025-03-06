from transformers import pipeline

# Load sentiment analysis model
model_name = "distilbert-base-uncased"
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    sentiment_label = result["label"]
    sentiment_score = result["score"]

    return {
        "sentiment_label": sentiment_label,
        "sentiment_score": sentiment_score
    }

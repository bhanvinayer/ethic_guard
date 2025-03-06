from sentiment_analysis import analyze_sentiment

# List of corporate and marketing sentences with positive, negative, and neutral sentiments
sentences = [
    "Our company has achieved record profits this quarter.",  # Positive
    "We are excited to announce the launch of our new product line.",  # Positive
    "Customer satisfaction is our top priority.",  # Positive
    "The recent changes in management have led to significant improvements.",  # Positive
    "We regret to inform you that there will be a delay in your order.",  # Negative
    "Our team is dedicated to providing the best service possible.",  # Positive
    "The market conditions have been challenging, but we remain optimistic.",  # Neutral
    "We are committed to sustainability and reducing our environmental impact.",  # Positive
    "Our innovative solutions are designed to meet the needs of our clients.",  # Positive
    "We appreciate your continued support and loyalty.",  # Positive
    "The project has been delayed due to unforeseen circumstances.",  # Negative
    "There have been some issues with the recent product update.",  # Negative
    "We are working hard to resolve the problems reported by our customers.",  # Neutral
    "The feedback from our clients has been mixed.",  # Neutral
    "We apologize for any inconvenience caused by the recent changes."  # Negative
]

# Analyze sentiment for each sentence
for sentence in sentences:
    sentiment = analyze_sentiment(sentence)
    print(f"Sentence: {sentence}")
    print(f"Sentiment: {sentiment}\n")

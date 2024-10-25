from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

if __name__ == "__main__":
    sample_text = "I love using Python for data science!"
    sentiment = analyze_sentiment(sample_text)
    print(f"Text: {sample_text}")
    print(f"Sentiment: {sentiment}")

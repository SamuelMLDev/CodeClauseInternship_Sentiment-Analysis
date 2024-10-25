import csv
import os
import logging
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("sentiment_analysis.log"),
        logging.StreamHandler()
    ]
)

def initialize_csv(filename='sentiment_results.csv'):
    """
    Initializes the CSV file with headers if it doesn't already exist.
    """
    if not os.path.exists(filename):
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'Text',
                    'Sentiment_TextBlob',
                    'Polarity_TextBlob',
                    'Subjectivity_TextBlob',
                    'Sentiment_VADER',
                    'Compound_VADER'
                ])
            logging.info(f"Initialized '{filename}' with headers.")
        except Exception as e:
            logging.error(f"An error occurred while initializing the CSV file: {e}")

def analyze_sentiment_textblob(text):
    """
    Analyzes the sentiment of the provided text using TextBlob.
    Returns the sentiment category, polarity, and subjectivity.
    """
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        logging.info(f"TextBlob Analysis - Text: '{text}' | Sentiment: {sentiment} | Polarity: {polarity} | Subjectivity: {subjectivity}")
        return sentiment, polarity, subjectivity
    except Exception as e:
        logging.error(f"An error occurred during TextBlob sentiment analysis: {e}")
        return "Error", 0.0, 0.0

def analyze_sentiment_vader(text, sia):
    """
    Analyzes the sentiment of the provided text using VADER.
    Returns the sentiment category and compound score.
    """
    try:
        scores = sia.polarity_scores(text)
        compound = scores['compound']

        if compound >= 0.05:
            sentiment = "Positive"
        elif compound <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        logging.info(f"VADER Analysis - Text: '{text}' | Sentiment: {sentiment} | Compound Score: {compound}")
        return sentiment, compound
    except Exception as e:
        logging.error(f"An error occurred during VADER sentiment analysis: {e}")
        return "Error", 0.0

def save_results(text, sentiment_tb, polarity_tb, subjectivity_tb, sentiment_vader, compound_vader, filename='sentiment_results.csv'):
    """
    Saves the sentiment analysis results to a CSV file.
    """
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                text,
                sentiment_tb,
                polarity_tb,
                subjectivity_tb,
                sentiment_vader,
                compound_vader
            ])
        logging.info(f"Saved analysis results for text: '{text}'")
    except Exception as e:
        logging.error(f"An error occurred while saving the results: {e}")

def main():
    """
    The main function that runs the sentiment analysis tool.
    """
    initialize_csv()
    logging.info("Welcome to the Sentiment Analysis Tool!")
    print("Welcome to the Sentiment Analysis Tool!")
    print("Type 'exit' to quit the program.\n")

    # Initialize VADER Sentiment Analyzer
    try:
        sia = SentimentIntensityAnalyzer()
        logging.info("Initialized VADER Sentiment Analyzer.")
    except Exception as e:
        logging.error(f"Failed to initialize VADER Sentiment Analyzer: {e}")
        print("Failed to initialize VADER Sentiment Analyzer. Exiting program.")
        return

    # Initialize sentiment counts
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0, "Error": 0}

    while True:
        user_input = input("Enter a sentence or review to analyze its sentiment: ").strip()
        if user_input.lower() == 'exit':
            print("\nSession Summary:")
            logging.info("User initiated exit.")
            for sentiment, count in sentiment_counts.items():
                print(f"{sentiment}: {count}")
            print("Thank you for using the Sentiment Analysis Tool!")
            logging.info("Exiting the sentiment analysis tool.")
            break
        elif not user_input:
            logging.warning("Empty input detected.")
            print("Empty input detected. Please enter a valid sentence or review.\n")
            continue

        # Analyze with TextBlob
        sentiment_tb, polarity_tb, subjectivity_tb = analyze_sentiment_textblob(user_input)
        print(f"\n[TextBlob] Sentiment: {sentiment_tb}")
        print(f"[TextBlob] Polarity: {polarity_tb}")
        print(f"[TextBlob] Subjectivity: {subjectivity_tb}\n")

        # Analyze with VADER
        sentiment_vader, compound_vader = analyze_sentiment_vader(user_input, sia)
        print(f"[VADER] Sentiment: {sentiment_vader}")
        print(f"[VADER] Compound Score: {compound_vader}\n")

        # Save results if both analyses are successful
        if sentiment_tb != "Error" and sentiment_vader != "Error":
            save_results(
                user_input,
                sentiment_tb,
                polarity_tb,
                subjectivity_tb,
                sentiment_vader,
                compound_vader
            )
            print("Analysis results saved to 'sentiment_results.csv'.\n")
            sentiment_counts[sentiment_tb] += 1
            sentiment_counts[sentiment_vader] += 1
        else:
            sentiment_counts["Error"] += 1
            print("An error occurred during analysis. Results not saved.\n")

if __name__ == "__main__":
    # Ensure NLTK data is downloaded
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        logging.info("Downloading VADER lexicon...")
        nltk.download('vader_lexicon')

    main()

# Sentiment Analysis Tool

## Overview

Welcome to the **Sentiment Analysis Tool**! This Python-based application allows users to analyze the sentiment of their input text, categorizing it as **Positive**, **Negative**, or **Neutral**. Leveraging both **TextBlob** and **VADER** from the `nltk` library, this tool provides a comprehensive sentiment analysis experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)

## Features

- **Dual Analysis Engines:** Utilizes both TextBlob and VADER for accurate sentiment detection.
- **Logging:** Implements logging to track events and errors.
- **CSV Logging:** Saves each analysis result to a CSV file for record-keeping.
- **Session Summary:** Provides a summary of sentiments analyzed during a session.
- **Error Handling:** Gracefully handles unexpected inputs and errors.
  


## Installation

Follow these steps to set up the Sentiment Analysis Tool on your local machine.

### **Prerequisites**

- **Python 3.7 or higher:** Ensure Python is installed. Download from [Python's official website](https://www.python.org/downloads/).

- **Git:** Ensure Git is installed. Download from [Git's official website](https://git-scm.com/downloads).

### **Step-by-Step Guide**

1. **Clone the Repository**

   Open your terminal or command prompt and run:

   ```bash
   git clone https://github.com/SamuelMLDev/CodeClauseInternship_Sentiment-Analysis.git
   ```

   Navigate into the project directory:

   ```bash
   cd CodeClauseInternship_Sentiment-Analysis
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK Data**

   The application relies on certain NLTK datasets. Run the following commands in your terminal:

   ```bash
   python
   ```

   Once in the Python interactive shell, execute:

   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

   After the download completes, exit the shell:

   ```python
   exit()
   ```

5. **Run the Application**

   Execute the sentiment analysis script:

   ```bash
   python sentiment_analysis.py
   ```

   **Alternatively,** if you're using an IDE like Visual Studio Code, you can run the script directly within the editor.

## Usage

Once the application is running, follow these steps:

1. **Input Text:** When prompted, enter a sentence or review you wish to analyze.

   ```
   Enter a sentence or review to analyze its sentiment: I absolutely love this new phone!
   ```

2. **View Results:** The tool will display sentiment analysis results from both TextBlob and VADER.

   ```
   [TextBlob] Sentiment: Positive
   [TextBlob] Polarity: 0.3352272727272727
   [TextBlob] Subjectivity: 0.5272727272727272

   [VADER] Sentiment: Positive
   [VADER] Compound Score: 0.5

   Analysis results saved to 'sentiment_results.csv'.
   ```

3. **Exit the Tool:** To quit the application, type `exit` when prompted.

   ```
   Enter a sentence or review to analyze its sentiment: exit

   Session Summary:
   Positive: 2
   Negative: 1
   Neutral: 0
   Error: 0
   Thank you for using the Sentiment Analysis Tool!
   ```


## Dependencies

All required Python packages are listed in `requirements.txt`. Here's a summary:

- **TextBlob:** Simplifies text processing tasks like sentiment analysis.
- **nltk:** Natural Language Toolkit, provides tools for working with human language data.
- **VADER:** Valence Aware Dictionary and sEntiment Reasoner, optimized for sentiments expressed in social media.
- **logging:** Built-in Python module for tracking events that happen when software runs.

To install dependencies manually, you can run:

```bash
pip install textblob nltk
```

The tech stack includes:

Python, TextBlob, NLTK, VADER, Git, GitHub, Virtual Environment (venv), Logging Module, CSV, Visual Studio Code

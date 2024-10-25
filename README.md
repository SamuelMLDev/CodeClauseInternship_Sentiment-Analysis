# Sentiment Analysis Tool

## Overview

Welcome to the **Sentiment Analysis Tool**! This Python-based application allows users to analyze the sentiment of their input text, categorizing it as **Positive**, **Negative**, or **Neutral**. Leveraging both **TextBlob** and **VADER** from the `nltk` library, this tool provides a comprehensive sentiment analysis experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
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

 **Navigate into the project directory:**
   ```bash
   cd CodeClauseInternship_Sentiment-Analysis
   ```
   
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```
3. **Activate the Virtual Envrionment**
Windows:
```bash
venv\Scripts\activate
```
5. **Install Dependencies**
macOS/Linux:
```bash
source venv/bin/activate
```
7. **Download NLTK Data**
The application relies on certain NLTK datasets. Run the following commands in your terminal:
```bash
python
```

Once in the Python interactive shell, execute:

```bash
import nltk
nltk.download('vader_lexicon')
```

After the download completes, exit the shell:
```
exit()
```

9. **Run the Application**

Execute the sentiment analysis script:
```
python sentiment_analysis.py
```
Alternatively, if you're using an IDE like Visual Studio Code, you can run the script directly within the editor.


## Usage

Once the application is running, follow these steps:

1. Input Text: When prompted, enter a sentence or review you wish to analyze.

```bash
Enter a sentence or review to analyze its sentiment: I absolutely love this new phone!
```

2. View Results: The tool will display sentiment analysis results from both TextBlob and VADER.

```bash
[TextBlob] Sentiment: Positive
[TextBlob] Polarity: 0.3352272727272727
[TextBlob] Subjectivity: 0.5272727272727272

[VADER] Sentiment: Positive
[VADER] Compound Score: 0.5

Analysis results saved to 'sentiment_results.csv'.
```

3. Exit the Tool: To quit the application, type exit when prompted.

```
Copy code
Enter a sentence or review to analyze its sentiment: exit

Session Summary:
Positive: 2
Negative: 1
Neutral: 0
Error: 0
Thank you for using the Sentiment Analysis Tool!
```

## Dependencies

All required Python packages are listed in requirements.txt. Here's a summary:

1. TextBlob: Simplifies text processing tasks like sentiment analysis.
2. nltk: Natural Language Toolkit, provides tools for working with human language data.
3. VADER: Valence Aware Dictionary and sEntiment Reasoner, optimized for sentiments expressed in social media.
4. logging: Built-in Python module for tracking events that happen when software runs.

To install dependencies manually, you can run:

```bash
pip install textblob nltk
```

## Usage

After completing the installation steps, you can run the Drone AI Autonomous Navigation System to start the drone's autonomous navigation. Follow the instructions below to ensure the system operates correctly.

### 1. Ensure the Virtual Environment is Activated

Before running the application, make sure your virtual environment is activated. This ensures that all dependencies are correctly loaded.

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

> **Note:** Your terminal prompt should start with `(venv)` indicating that the virtual environment is active.

### 2. Run the Application

Execute the main application script to start the autonomous navigation system.

```bash
python src/main.py
```

- **What Happens Next:**
  - A window titled **"Drone AI - Object Detection, SLAM, and Rule-Based Navigation"** will open, displaying the live feed from your webcam.
  - The system will begin processing the video feed to detect objects and update the drone's position using SLAM.

### 3. Interacting with the Application

#### A. Object Detection

- **Visual Indicators:**
  - Detected objects such as people, cars, or bicycles will be highlighted with bounding boxes and labeled accordingly.
  - **Faces:** Highlighted with green rectangles.
  - **Other Objects:** Highlighted with blue bounding boxes and labels.

#### B. SLAM (Simultaneous Localization and Mapping)

- **Pose Updates:**
  - The system calculates the drone's current position relative to the target destination.
  - Console logs will display the drone's pose, e.g., `Pose: [x, y, z]`.

- **Map Visualization:**
  - Upon exiting the application, a window titled **"Drone AI - Map"** will display accumulated map points representing the drone's movement.

#### C. Rule-Based Navigation

- **Action Display:**
  - The chosen navigation action (e.g., "Move Forward," "Turn Right," "Stop") will be overlaid on the video feed.
  - Corresponding action messages will be printed in the terminal.

- **Decision Logic:**
  - **No Obstacles Detected & Far from Target:** Action is "Move Forward."
  - **Obstacle Detected:** Action is "Turn Right" to avoid collision.
  - **Near Target:** Action is "Stop" upon reaching the destination.

### 4. Controls

- **Exit the Application:**
  - Press the `q` key in the video window to terminate the application gracefully.


### 5. Troubleshooting

If you encounter issues while running the application, consider the following troubleshooting steps:

#### A. No Video Stream

- **Check Webcam Connection:**
  - Ensure your webcam is properly connected and not being used by another application.
  
- **Verify Video Source:**
  - If you're using an external camera, ensure it's selected correctly in the code (currently set to `0` for the default webcam).
  
- **Error Messages:**
  - Look for any error messages in the terminal that might indicate issues with video capture.

#### B. Objects Not Detected

- **Lighting Conditions:**
  - Ensure adequate lighting for the camera to capture clear images.
  
- **Model Accuracy:**
  - Verify that the YOLOv5 model is correctly loaded and functioning.
  
- **Test with Clear Objects:**
  - Use high-contrast objects to see if detection improves.

#### C. Pose Not Updating

- **SLAM Module Issues:**
  - Ensure that the SLAM module is correctly implemented and receiving input from the video frames.
  
- **Console Logs:**
  - Look for any errors or warnings related to SLAM in the terminal.

#### D. Actions Not Displaying Correctly

- **Rule Logic:**
  - Double-check the rule-based decision-making logic in your `main.py` to ensure it's correctly interpreting the state and making appropriate decisions.
  
- **Console vs. Video Feed:**
  - Ensure that both the console and video overlay are correctly linked to the action outputs.

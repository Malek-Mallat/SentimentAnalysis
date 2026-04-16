# 🎬 Movie Review Sentiment AI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.21.0-orange)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

## 📌 Overview
A smart web application for sentiment analysis based on Deep Learning (Recurrent Neural Network - LSTM). This project allows real-time analysis of movie reviews or free text to determine if the expressed opinion is **Positive** or **Negative**, providing a precise confidence score.

🔗 **Test the live application:** [https://sentiment-ai-232311198521.us-central1.run.app/]

## ✨ Key Features
- 🧠 **Advanced AI Model:** Powered by an RNN (LSTM) model built with Keras and TensorFlow.
- ⚡ **Real-Time:** Instant sentiment predictions via a fluid and responsive web interface.
- 🧹 **Automatic Cleaning:** Smart text preprocessing (HTML tag removal with BeautifulSoup, text standardization).
- 🐳 **Deployment Ready:** Containerized with Docker for easy and optimized deployment on **Google Cloud (Cloud Run)**, as well as other platforms.

## 🗂 Project Structure
```text
├── app.py                 # Main Flask application (API and Web)
├── Dockerfile             # Docker configuration file
├── requirements.txt       # Python project dependencies
├── rnn_model.keras        # Pre-trained Deep Learning model
├── tokenizer_rnn.pkl      # Tokenizer for model preprocessing
└── templates/
    └── index.html         # User interface
```

## 🚀 Local Installation & Launch

### 1. Clone or download the repository
Ensure you have Python 3.8+ installed.

### 2. Install dependencies
It is recommended to use a virtual environment (venv).

```bash
pip install -r requirements.txt
```

### 3. Start the application
Run the Flask server:

```bash
python app.py
```

The application will be accessible at: `http://localhost:8080/`

## 🐳 Docker Deployment
You can build and run the Docker image locally in a few simple steps:

```bash
docker build -t sentiment-ai .
docker run -p 8080:8080 sentiment-ai
```

## ☁️ Google Cloud (Cloud Run) Deployment
The project is perfectly configured for a serverless deployment on **Google Cloud Run**.

### Quick deployment via the gcloud CLI:
```bash
# 1. Authenticate
gcloud auth login

# 2. Set your project
gcloud config set project [YOUR_PROJECT_ID]

# 3. Deploy the application (port 8080 is already configured)
gcloud run deploy sentiment-ai --source . --port 8080 --allow-unauthenticated
```
The secure public URL (HTTPS) will be provided at the end of the execution.

## 📊 Dataset
The model was trained on the famous **IMDB 50k Movie Reviews** dataset, a key reference in Natural Language Processing (NLP).

## 🛠 Technologies
- **Backend:** Flask, Gunicorn
- **Machine Learning:** TensorFlow, Keras, Numpy
- **Text Processing:** BeautifulSoup4, Regular Expressions (RegEx)
- **Frontend:** HTML/CSS (Jinja2 Templates)

from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from keras.utils import pad_sequences
from bs4 import BeautifulSoup
import re
import pickle

app = Flask(__name__)

MAX_LENGTH = 230
model_file = 'rnn_model.keras'
tokenizer_file = 'tokenizer_rnn.pkl'

model = tf.keras.models.load_model(model_file)
with open(tokenizer_file, 'rb') as f:
    tokenizer = pickle.load(f)

def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    return text

def predict_sentiment(text):
    cleaned = clean_text(text)
    sequence = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(sequence, maxlen=MAX_LENGTH, padding='pre')
    prediction = model.predict(padded)[0][0]
    if prediction >= 0.5:
        return "POSITIVE", float(prediction)
    else:
        return "NEGATIVE", float(1 - prediction)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('review', '')
    if not text:
        return render_template('index.html', error="Veuillez entrer au moins une critique.")
    
    # Séparer les reviews par saut de ligne
    reviews = [r.strip() for r in text.split('\n') if r.strip()]
    
    results = []
    pos_count = 0
    neg_count = 0
    
    for r in reviews:
        sentiment, confidence = predict_sentiment(r)
        results.append({
            'text': r,
            'sentiment': sentiment,
            'confidence': f"{confidence*100:.2f}%"
        })
        if sentiment == 'POSITIVE':
            pos_count += 1
        else:
            neg_count += 1
            
    return render_template('index.html',
                           results=results,
                           pos_count=pos_count,
                           neg_count=neg_count,
                           raw_text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
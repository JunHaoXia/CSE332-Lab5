from flask import Flask, render_template, request, jsonify
import pandas as pd
import random
app = Flask(__name__)
# Load your dataset
data = pd.read_csv("youtube_data.csv", encoding_errors='ignore')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
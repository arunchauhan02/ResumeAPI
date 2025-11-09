import nltk
nltk.download('stopwords')
from flask import Flask, request, jsonify
import os
from extractor import ExtractFromResume # import your function
import nltk
from werkzeug.utils import secure_filename

try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    nltk.download('stopwords')
app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract_api():
    data = request.json
    text = data.get("text", "")

    result = ExtractFromResume(text)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port, debug=False) 


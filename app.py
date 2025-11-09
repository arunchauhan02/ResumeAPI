
from flask import Flask, request, jsonify
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
    app.run(debug=True)

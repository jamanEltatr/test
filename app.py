from flask import Flask, render_template

app = Flask(__name__)

languages = [
    {"name": "Spanish", "flag": "es.png", "speakers": "534 million"},
    {"name": "French", "flag": "fr.png", "speakers": "280 million"},
    {"name": "German", "flag": "de.png", "speakers": "130 million"},
    {"name": "Japanese", "flag": "jp.png", "speakers": "128 million"},
    {"name": "Italian", "flag": "it.png", "speakers": "85 million"},
    {"name": "Russian", "flag": "ru.png", "speakers": "258 million"},
]

@app.route('/')
def home():
    return render_template('index.html', languages=languages)

if __name__ == '__main__':
    app.run(debug=True)

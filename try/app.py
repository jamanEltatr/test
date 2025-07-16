from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the main index.html page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Set debug=True for development.
    # Turn off debug=False for production for security and performance.
    app.run(debug=True)

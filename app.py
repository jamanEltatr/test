# app.py
from flask import Flask, send_from_directory

app = Flask(__name__)

# Route to serve the main index.html file
@app.route('/')
def serve_index():
    """Serves the index.html file from the current directory."""
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # Run the Flask development server
    # debug=True automatically reloads the server when you make code changes
    # and provides more detailed error messages.
    app.run(debug=True, port=5000) # You can change the port if 5000 is in use
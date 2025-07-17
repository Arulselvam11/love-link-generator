import os
import logging
from flask import Flask

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "your-secret-key-for-development")

# In-memory storage for MVP
love_links = {}

# Import routes
from routes import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
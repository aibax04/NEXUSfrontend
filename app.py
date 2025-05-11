from flask import Flask, request, jsonify, send_from_directory
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='.')
CORS(app, origins=["https://frontend-three-cyan-66.vercel.app"])

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query', '')
    
    # TODO: Implement your actual AI/chat logic here
    # For now, returning a simple response
    response = f"I received your message: {query}. This is a placeholder response."
    
    return jsonify({'answer': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 
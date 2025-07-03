from flask import Flask, request, jsonify
from flask_cors import CORS
from aws_bedrock import initialize_bedrock_client, invoke_bedrock_model
import json

app = Flask(__name__)
CORS(app)

client = initialize_bedrock_client()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'Prompt is required.'}), 400
    try:
        model_reply = invoke_bedrock_model(client, prompt)
        return jsonify({'response': model_reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 
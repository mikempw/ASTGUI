# app.py
from flask import Flask, send_from_directory, jsonify, request
import yaml
import os
from dotenv import load_dotenv, set_key
import tempfile
import shutil

app = Flask(__name__)

CONFIG_DIR = '/app/config'
ENV_FILE = '/app/.env'
ENV_SECRETS_FILE = '/app/env.device-secrets'

def load_yaml(filename):
    try:
        with open(os.path.join(CONFIG_DIR, filename), 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {}

def save_yaml(filename, data):
    with open(os.path.join(CONFIG_DIR, filename), 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def load_env(filename):
    if not os.path.exists(filename):
        return {}
    load_dotenv(filename)
    return {key: os.getenv(key) for key in os.environ}

def save_env(filename, data):
    # Create a temporary file
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as temp:
            for key, value in data.items():
                temp.write(f"{key}={value}\n")
        
        # Replace the original file with the temporary file
        shutil.move(path, filename)
    finally:
        # Clean up the temporary file in case of an error
        if os.path.exists(path):
            os.unlink(path)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/api/config/<config_type>', methods=['GET', 'POST'])
def handle_config(config_type):
    if request.method == 'GET':
        if config_type in ['ast_defaults', 'bigip_receivers']:
            return jsonify(load_yaml(f'{config_type}.yaml'))
        elif config_type == 'env':
            return jsonify(load_env(ENV_FILE))
    elif request.method == 'POST':
        data = request.json
        try:
            if config_type in ['ast_defaults', 'bigip_receivers']:
                save_yaml(f'{config_type}.yaml', data)
            elif config_type == 'env':
                save_env(ENV_FILE, data)
            return jsonify({"status": "success"})
        except Exception as e:
            app.logger.error(f"Error saving configuration: {str(e)}")
            return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
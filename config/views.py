from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import json
import os
import yaml

@ensure_csrf_cookie
def index(request):
    return render(request, 'config/index.html')

@require_http_methods(["POST"])
def save_ast_defaults(request):
    data = json.loads(request.body)
    config_path = data['configPath']
    ast_defaults = data['data']
    file_path = os.path.join(config_path, 'ast_defaults.yaml')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        yaml.dump(ast_defaults, f, default_flow_style=False)
    return JsonResponse({"status": "success", "message": "AST defaults saved successfully."})

@require_http_methods(["POST"])
def save_bigip_receivers(request):
    data = json.loads(request.body)
    config_path = data['configPath']
    bigip_receivers = data['data']
    file_path = os.path.join(config_path, 'bigip_receivers.yaml')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        yaml.dump(bigip_receivers, f, default_flow_style=False)
    return JsonResponse({"status": "success", "message": "BIG-IP receivers saved successfully."})

@require_http_methods(["POST"])
def save_env_variables(request):
    data = json.loads(request.body)
    config_path = data['configPath']
    env_variables = data['data']
    file_path = os.path.join(config_path, 'env_variables.yaml')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        yaml.dump(env_variables, f, default_flow_style=False)
    return JsonResponse({"status": "success", "message": "Environment variables saved successfully."})

@require_http_methods(["POST"])
def save_env_secrets(request):
    data = json.loads(request.body)
    config_path = data['configPath']
    env_secrets = data['data']
    file_path = os.path.join(config_path, 'env_secrets.yaml')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        yaml.dump(env_secrets, f, default_flow_style=False)
    return JsonResponse({"status": "success", "message": "Environment secrets saved successfully."})
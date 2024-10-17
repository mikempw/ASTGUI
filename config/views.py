from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import json
import os

@ensure_csrf_cookie
def index(request):
    return render(request, 'config/index.html')

@require_http_methods(["POST"])
def save_ast_defaults(request):
    data = json.loads(request.body)
    # Here you would typically save this to a configuration file or database
    # For this example, we'll just print it
    print("Saving AST Defaults:", data)
    return JsonResponse({"status": "success"})

@require_http_methods(["POST"])
def save_bigip_receivers(request):
    data = json.loads(request.body)
    # Here you would typically save this to a configuration file or database
    # For this example, we'll just print it
    print("Saving BIG-IP Receivers:", data)
    return JsonResponse({"status": "success"})

@require_http_methods(["POST"])
def save_env_variables(request):
    data = json.loads(request.body)
    # Process and save the data
    print("Saving Environment Variables:", data)
    return JsonResponse({"status": "success"})

@require_http_methods(["POST"])
def save_env_secrets(request):
    data = json.loads(request.body)
    # Process and save the data
    print("Saving Environment Secrets:", data)
    return JsonResponse({"status": "success"})
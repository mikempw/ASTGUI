from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_ast_defaults/', views.save_ast_defaults, name='save_ast_defaults'),
    path('save_bigip_receivers/', views.save_bigip_receivers, name='save_bigip_receivers'),
    path('save_env_variables/', views.save_env_variables, name='save_env_variables'),
    path('save_env_secrets/', views.save_env_secrets, name='save_env_secrets'),
]
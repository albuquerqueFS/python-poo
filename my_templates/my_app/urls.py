from django.urls import path
from . import views

# register the app name space

app_name = 'my_app'

urlpatterns = [
    path('index', views.index_view, name='index'),
    path('simple/', views.simple_view, name='simple'),
] 
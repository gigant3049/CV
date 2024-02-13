from django.urls import path
from .views import detail

app_name = 'articles'

urlpatterns = [
    path('detail/<slug:slug>/', detail, name='detail', )
]

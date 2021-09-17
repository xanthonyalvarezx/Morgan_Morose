from django.urls import path
from .views import post_detail

urlpatterns = [
path('postdetail/<int:post_id>/', post_detail),
    
]

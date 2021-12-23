from django.urls import path
from .views import post_detail, music, fashion, food, travel

urlpatterns = [
    path('postdetail/<int:post_id>/', post_detail),
    path('music', music),
    path('fashion', fashion),
    path('food', food),
    path('travel', travel)

]

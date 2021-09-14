from django.urls import path
from user_admin.views import add_post, add_author
urlpatterns = [
    path('createpost/', add_post ),
    path('createuser/', add_author)
]

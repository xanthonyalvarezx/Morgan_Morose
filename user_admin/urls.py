from django.urls import path
from user_admin.views import add_post, add_author, image_upload, login_view, logout_view
urlpatterns = [
    path('createpost/', add_post, name='createpost' ),
    path('createuser/', add_author, name='createuser'),
    path('imageupload/',image_upload ),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view')
]

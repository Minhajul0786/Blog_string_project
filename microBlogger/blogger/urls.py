from django.urls import path
from blogger.views import registeration,loginUser,display_posts,create_post,logout, validate_username, comment,logout_user
app_name = "blogger"
urlpatterns = [
    path('register/', registeration , name='register'),
    path('login/', loginUser , name='login'),
    path('display/', display_posts, name='display'),
    path('create/', create_post, name='create'),
    path('logout/', logout_user, name='logout'),
    path('ajax/validate_username/',validate_username, name = 'validate_username' ),
    path('ajax/comment/', comment , name= 'comment'),
]

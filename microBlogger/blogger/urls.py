from django.urls import path
from blogger.views import registeration,loginUser,display_posts,create_post
app_name = "blogger"
urlpatterns = [
    path('register/', registeration , name='register'),
    path('login/', loginUser , name='login'),
    path('display/', display_posts, name='display'),
    path('create/', create_post, name='create'),
]

from django.urls import path
from blogger.views import registeration,loginUser
app_name = "blogger"
urlpatterns = [
    path('register/', registeration , name='register'),
    path('login/', loginUser , name='login'),
]
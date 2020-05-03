from django.urls import path
from .views import ViewSignUp

urlpatterns = [
    path('signup/', ViewSignUp.as_view(), name ='signup'),
]
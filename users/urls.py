from django.urls import path
from .views import ViewSignUp, ViewSignUpAfter
# ViewRessetpassword

urlpatterns = [
    path('signup/', ViewSignUp.as_view(), name ='signup'),
    path('signup_done/', ViewSignUpAfter.as_view(), name ='signup_done'),
    # path('users/password_reset/', ViewRessetpassword.as_view(), name ='reset_password'),
]
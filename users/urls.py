from django.urls import path
from users.views import UserApiView, UserApiViewDetail, LoginView, UserView, LogoutView

url_users = [
    path('v1/users', UserApiView.as_view()),
    path('v1/users/<int:id>', UserApiViewDetail.as_view()),
    path('v1/login', LoginView.as_view()),
    path('v1/logout', LogoutView.as_view()),
    path('v1/user', UserView.as_view()),
]
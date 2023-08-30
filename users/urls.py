from django.urls import path
from users.views import UserApiView, UserApiViewDetail

url_users = [
    path('v1/users', UserApiView.as_view()),
    path('v1/users/<int:id>', UserApiViewDetail.as_view()),
    # path('v1/cuestions', OpenAiMonitoring.as_view()),
]
from django.urls import path
from users.views import UserApiView, UserApiViewDetail, AuthenticateUserView, CreateTokenView

url_users = [
    path('v1/users', UserApiView.as_view()),
    path('v1/users/<int:id>', UserApiViewDetail.as_view()),
    path('v1/token', CreateTokenView.as_view()),
    path('v1/authorized', AuthenticateUserView.as_view()),
    # path('v1/userToken', loginToken.as_view())
    # path('v1/cuestions', OpenAiMonitoring.as_view()),
]
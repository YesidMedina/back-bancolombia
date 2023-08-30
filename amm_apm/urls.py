from django.urls import path
from amm_apm.views import AmmApmApiView, AmmApmApiViewDetail, EmailAmmApmApiView, EmailAmmApmApiViewDetail

url_amm_apm = [
    path('v1/amm_apm', AmmApmApiView.as_view()),
    path('v1/amm_apm/<int:id>', AmmApmApiViewDetail.as_view()),
    path('v1/email_apm', EmailAmmApmApiView.as_view()),
    path('v1/email_apm/<int:id>', EmailAmmApmApiViewDetail.as_view()),
]

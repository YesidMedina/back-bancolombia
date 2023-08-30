from django.urls import path
from amm_cloud.views import AmmCloudApiView, AmmCloudApiViewDetail, EmailAmmCloudApiView, EmailAmmCloudApiViewDetail

url_amm_cloud = [
    path('v1/amm_cloud', AmmCloudApiView.as_view()),
    path('v1/amm_cloud/<int:id>', AmmCloudApiViewDetail.as_view()),
    path('v1/email_cloud', EmailAmmCloudApiView.as_view()),
    path('v1/email_cloud/<int:id>', EmailAmmCloudApiViewDetail.as_view()),
]

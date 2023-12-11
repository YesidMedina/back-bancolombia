from django.urls import path
from amm_cloud.views import AmmCloudApiView, AmmCloudApiViewDetail, AmmCloudRetiredApiView, EmailAmmCloudApiView, EmailAmmCloudApiViewDetail, EmailAmmCloudGetApiView

url_amm_cloud = [
    path('v1/amm_cloud', AmmCloudApiView.as_view()),
    path('v1/retired_cloud', AmmCloudRetiredApiView.as_view()),
    path('v1/amm_cloud/<int:id>', AmmCloudApiViewDetail.as_view()),
    path('v1/email_cloud', EmailAmmCloudGetApiView.as_view()),
    path('v1/email_filter', EmailAmmCloudGetApiView.as_view()),
    path('v1/email_cloud/<int:id>', EmailAmmCloudApiViewDetail.as_view()),
]

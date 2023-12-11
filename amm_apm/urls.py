from django.urls import path
from amm_apm.views import AmmApmApiView, AmmApmApiViewDetail, EmailAmmApmApiView, EmailAmmApmApiViewDetail, AmmApmRetiredApiView, EmailAmmApmGetApiView, GraphicsAmmApm, GraphicsAmmApmFull, GraphicsFilialAmmApm, JobAmmApmRetiredApiView, JobAmmApmApiView, JobApmApiViewDetail, GraphicsJobAmmApm

url_amm_apm = [
    path('v1/amm_apm', AmmApmApiView.as_view()),
    path('v1/retired_apm', AmmApmRetiredApiView.as_view()),
    path('v1/amm_apm/<int:id>', AmmApmApiViewDetail.as_view()),
    path('v1/email_apm', EmailAmmApmGetApiView.as_view()),
    path('v1/email_create_apm', EmailAmmApmApiView.as_view()),
    path('v1/email_apm/<int:id>', EmailAmmApmApiViewDetail.as_view()),
    path('v1/dashboard_apm', GraphicsAmmApm.as_view()),
    path('v1/dashboardfull_apm', GraphicsAmmApmFull.as_view()),
    path('v1/dashboard_filial_apm', GraphicsFilialAmmApm.as_view()),
    path('v1/jobs', JobAmmApmApiView.as_view()),
    path('v1/jobs_create', JobAmmApmApiView.as_view()),
    path('v1/retired_jobs', JobAmmApmRetiredApiView.as_view()),
    path('v1/jobs/<int:id>', JobApmApiViewDetail.as_view()),
    path('v1/total_jobs', GraphicsJobAmmApm.as_view())   
]

from django.urls import path
from amm_im.views import AmmImApiView, AmmImApiViewDetail, EmailAmmImApiViewDetail, GraphicsAmmIm, GraphicsAmmImFull, AmmImRetiredApiView, DetailArryView, EmailAmmImGetApiView, GraphicsFilialAmmIm, BaseLineAmmImApiView, EmailAmmImApiView

url_amm_im = [
    path('v1/amm_im', AmmImApiView.as_view()),
    path('v1/retired', AmmImRetiredApiView.as_view()),
    path('v1/amm_im/<int:id>', AmmImApiViewDetail.as_view()), 
    path('v1/several', AmmImApiViewDetail.as_view()), 
    path('v1/email', EmailAmmImGetApiView.as_view()),   
    path('v1/email_create', EmailAmmImApiView.as_view()),
    path('v1/email/<int:id>', EmailAmmImApiViewDetail.as_view()),
    path('v1/email/<int:id>', EmailAmmImApiViewDetail.as_view()),
    path('v1/dashboard', GraphicsAmmIm.as_view()),
    path('v1/dashboardfull', GraphicsAmmImFull.as_view()),
    path('v1/dashboard_filial', GraphicsFilialAmmIm.as_view()),
    # path('v1/excel', ExportIMportExcel.as_view())
    path('v1/masive', DetailArryView.as_view()),
    path('v1/baseline', BaseLineAmmImApiView.as_view())


    
]

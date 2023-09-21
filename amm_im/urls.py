from django.urls import path
from amm_im.views import AmmImApiView, AmmImApiViewDetail, EmailAmmImApiView, EmailAmmImApiViewDetail, GraphicsAmmIm, GraphicsAmmImFull, AmmImRetiredApiView, FilterEmailAmmIm

url_amm_im = [
    path('v1/amm_im', AmmImApiView.as_view()),
    path('v1/amm_im/<int:id>', AmmImApiViewDetail.as_view()),
    path('v1/amm_im_several', AmmImApiViewDetail.as_view()),
    path('v1/email', EmailAmmImApiView.as_view()),
    path('v1/email/<int:id>', EmailAmmImApiViewDetail.as_view()),
    path('v1/email/<int:id>', EmailAmmImApiViewDetail.as_view()),
    path('v1/dashboard', GraphicsAmmIm.as_view()),
    path('v1/dashboardfull', GraphicsAmmImFull.as_view()),
    # path('v1/excel', ExportIMportExcel.as_view())
    path('v1/retired', AmmImRetiredApiView.as_view()),
    path('v1/filter_email', FilterEmailAmmIm.as_view())
]

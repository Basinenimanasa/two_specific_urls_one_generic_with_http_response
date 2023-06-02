from  django.urls import path
from gt.views import *
app_name='gt'
urlpatterns=[
    path('hardhik/',hardhik,name='hardhik'),
]
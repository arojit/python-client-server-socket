from django.urls import path
from . import views

urlpatterns = [
    path('request-for-action',views.requestForActionDef,name='requestForActionDef'),
]
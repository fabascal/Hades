from django.urls import path
from core.erp.views import myfirstview, mysecondview

urlpatterns = {
    path('uno/', myfirstview),
    path('dos/', mysecondview)
}
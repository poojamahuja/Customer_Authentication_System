from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('user', views.UserList, basename='user')
router.register('customerdetail', views.CustomerDetail, basename='customerdetail')

urlpatterns = [
    path('', include(router.urls)),
]

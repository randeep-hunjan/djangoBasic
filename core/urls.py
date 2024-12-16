from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CompanyViewSet, login_view, logout_view, register_view

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('companies', CompanyViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('', include(router.urls)),
]

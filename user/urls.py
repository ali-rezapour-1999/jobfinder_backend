from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet

router = DefaultRouter()
router.register('auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('auth/register/',
         AuthViewSet.as_view({'post': 'register'}), name='register'),
    path('auth/verify-email/',
         AuthViewSet.as_view({'post': 'verify_email'}), name='verify_email'),
    path('auth/login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('auth/verify-login/',
         AuthViewSet.as_view({'post': 'verify_login'}), name='verify_login'),
]

urlpatterns += router.urls

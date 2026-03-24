from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('login/', views.login_user, name='login-user'),
    path('login-page/', views.login_page, name='login-page'),
    path('register/', views.register_user, name='register-user'),
    path('logout/', views.logout_user, name='logout-user'),
    path('current-user/', views.current_user, name='current-user'),
    path('', include(router.urls)),
]

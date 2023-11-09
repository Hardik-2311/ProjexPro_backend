from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projexApp.views import *
from projexApp.views.Oauth import login_direct, check_login, Oauth2_Login, logout_direct

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"tasks", ProjectViewSet)
router.register(r"goals", ProjectViewSet)
router.register(r"feedbacks", ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", check_login),
    path("login", login_direct),
    path("check_login", check_login),
    path("oauth2_login/", Oauth2_Login),
    path("logout", logout_direct),
]

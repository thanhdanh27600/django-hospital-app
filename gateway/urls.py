from django.urls import path, include
from .views import LoginView, RefreshView, RegisterView, GetSecuredInfo

urlpatterns = [
    # path("", include("hospital_app.urls")),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('refresh', RefreshView.as_view()),
    path('secured-info', GetSecuredInfo.as_view()),
]

from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    # path('login/', LoginView.as_view(), {'template_name':'login.html'}),
]
